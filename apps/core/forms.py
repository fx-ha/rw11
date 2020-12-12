from django import forms
from django.utils import timezone
from django.db.models import Q

from apps.event.models import Event


class ContactForm(forms.Form):
    message_name = forms.CharField(required=True)
    message_email = forms.EmailField(required=True)
    message_note = forms.CharField(required=True)
    message_event = forms.CharField(required=False)
    message_persons = forms.CharField(required=False)