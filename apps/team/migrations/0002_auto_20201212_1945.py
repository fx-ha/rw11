# Generated by Django 3.1.4 on 2020-12-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/team/', verbose_name='Bild'),
        ),
    ]
