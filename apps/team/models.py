import datetime

from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField

class TeamMember(models.Model):
    """Model representing a member for the team site"""
    first_name = models.CharField("Vorname", max_length=50)

    last_name = models.CharField("Nachname", max_length=50)

    birthday = models.DateField("Geburtstag", blank=True, null=True)
    
    description = RichTextField("Bio", blank=True, null=True)

    position = models.IntegerField(
        "Position", 
        default=90,
        help_text="An welcher Stelle wird die Person in der Teamübersicht aufgelistet? 1 = oben, 2 unter 1, 3 unter 2 usw."
    )

    active = models.BooleanField(
        "Aktiv?",
        default=True,
        help_text="Ist die Person derzeit aktives Mitglied von RW11?"
    )

    image = models.ImageField('Bild', null=True, blank=True, upload_to='media/images/team/')

    class Meta:
        verbose_name = 'Teammitglied'
        verbose_name_plural = 'Teammitglieder'    
        ordering = ['position']

    def __str__(self):
        """String for representing the Model object (in Admin site etc)."""
        return self.last_name        

    def get_absolute_url(self):
        """Returns the url to access a detail record for this team member."""
        return reverse("event_detail", kwargs={"pk": self.pk})

    def name(self):
        """Combines first name and last name"""
        return self.first_name + ' ' + self.last_name

    def age(self):
        """Calculate the age in years by using birthday and current date"""
        birthday = self.birthday
        if (birthday):
            today = datetime.date.today()        
            age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
            return age