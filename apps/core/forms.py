from django import forms
from django.utils import timezone
from django.db.models import Q

from apps.event.models import Event


class ContactForm(forms.Form):
    message_name = forms.CharField(required=True)
    message_email = forms.EmailField(required=True)
    message_note = forms.CharField(required=True)

    events = Event.objects.filter(Q(startdate__gte=timezone.now()) | Q(enddate__gte=timezone.now()))
    if events:
        message_event = forms.CharField(required=False)
        message_persons = forms.CharField(required=False)