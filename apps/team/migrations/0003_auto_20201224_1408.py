# Generated by Django 3.1.4 on 2020-12-24 13:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20201212_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Bild'),
        ),
    ]