from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Event(models.Model):
    """Model representing an event"""
    title = models.CharField("Titel", max_length=200)

    short_description = models.TextField("Kurze Beschreibung", max_length=240, null=True, blank=True)

    description = RichTextField("Beschreibung", blank=True, null=True)

    startdate = models.DateField("Starttermin")

    enddate = models.DateField("Letzter Termin", null=True, blank=True)

    starttime = models.TimeField("Uhrzeit - Beginn", null=True, blank=True)

    endtime = models.TimeField("Uhrzeit - Ende", null=True, blank=True)

    bookable = models.BooleanField("Reservierbar", default=True)

    class Meta:
        verbose_name = 'Veranstaltung'
        verbose_name_plural = 'Veranstaltungen'
        ordering = ['-startdate']

    def __str__(self):
        """String for representing the Model object (in Admin site etc)."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this event."""
        return reverse("event_detail", kwargs={"pk": self.pk})


class Image(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)
    image = CloudinaryField(
        'Bild',
        null=True,
        blank=True,
        transformation=[{'width': 700, 'height': 700, 'crop': "limit"}],
        format="jpg",
    )

    class Meta:
        verbose_name = 'Bild'
        verbose_name_plural = 'Bilder'