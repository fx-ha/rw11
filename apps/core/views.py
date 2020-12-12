import json
import urllib.request
import urllib.parse

from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

from apps.event.models import Event
from .forms import ContactForm


def index(request):
    """View function for homepage of site"""
    # Return the current 4 events
    events = Event.objects.filter(Q(startdate__gte=timezone.now()) | Q(enddate__gte=timezone.now()))
    if events:
        events = events.order_by('startdate')[:4]
        has_current_events = True
    # when no exist return last event
    else:    
        events = Event.objects.filter(startdate__lt=timezone.now()).order_by('-startdate')[:1]
        has_current_events = False
    context = {
        'events': events,
        'has_current_events': has_current_events,
    }    
    return render(request, 'core/index.html', context)


def imprint(request):
    """View function for imprint"""
    return render(request, 'core/imprint.html')    


def privacy_policy(request):
    """View function for privacy policy"""
    return render(request, 'core/privacy_policy.html')


def contact(request):
    """View function for contact"""    
    events = Event.objects.filter(Q(startdate__gte=timezone.now()) | Q(enddate__gte=timezone.now()))

    if request.method == 'GET':
        context = {
                'events': events,
        }
        return render(request, 'core/contact.html', context)        

    if request.method == 'POST':          
        form = ContactForm(request.POST)

        if form.is_valid():
            message_name = form.cleaned_data['message_name']
            message_email = form.cleaned_data['message_email']
            message_note = form.cleaned_data['message_note']

            if Event.objects.filter(Q(startdate__gte=timezone.now()) | Q(enddate__gte=timezone.now())).exists():
                message_event = form.cleaned_data['message_event']
                message_persons = form.cleaned_data['message_persons']
            else:     
                message_event = False
                message_persons = False

            """Begin reCAPTCHA validation"""
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)

            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            """End reCAPTCHA validation"""

            if result['success'] and result['score'] > 0.4:
                if message_event and message_persons:
                    subject = 'Reservierung "'
                    subject += message_event
                    subject += '" von '
                    subject += message_name
                    body = message_name
                    body += ' möchte für die Veranstaltung '
                    body += message_event
                    body += ' insgesamt '
                    body += message_persons
                    body += ' Karten reservieren. '
                    body += message_name
                    body += ' ist zu erreichen unter: '
                    body += message_email
                    body += '.'
                    if message_note:
                        body += ' Folgende Mitteilung wurde angehängt: '
                        body += message_note
                else:
                    subject = 'Kontaktanfrage von ' + message_name
                    body = message_name
                    body += ', zu erreichen unter: '
                    body += message_email
                    body += ', sendet folgende Mitteilung'
                    if message_event:
                        body += ' zur Veranstaltung '
                        body += message_event
                    body += ': '    
                    body += message_note

                recipients = ['felixha@protonmail.com']

                # wenn Email-Versand-Fehler
                try:
                    send_mail(subject, body, message_email, recipients)
                except BadHeaderError:
                    context = {
                        'events': events,
                        'response': 'header_error',
                    }
                    return render(request, 'core/contact.html', context)

                # alles erfolgreich
                context = {
                    'events': events,
                    'response': 'success',
                }
                return render(request, 'core/contact.html', context)

            # wenn Captcha Fehler
            else:
                context = {
                    'events': events,
                    'response': 'captcha_error',
                }
                return render(request, 'core/contact.html', context)

        # wenn Formular ungültig
        else:
            context = {
                'events': events,
                'response': 'form_error',
            }
            return render(request, 'core/contact.html', context)
