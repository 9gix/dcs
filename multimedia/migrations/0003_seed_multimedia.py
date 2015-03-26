# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command


def seed_multimedia(apps, schema_editor):
    call_command('loaddata', 'multimedia_data', app_label='multimedia')

def delete_multimedia(apps, schema_editor):
    Book = apps.get_model('multimedia', 'Book')
    Music = apps.get_model('multimedia', 'Music')
    Album = apps.get_model('multimedia', 'Album')
    AlbumMusic = apps.get_model('multimedia', 'AlbumMusic')
    Multimedia = apps.get_model('multimedia', 'Multimedia')
    Category = apps.get_model('multimedia', 'Category')
    MultimediaReview = apps.get_model('multimedia', 'MultimediaReview')
    MultimediaContent = apps.get_model('multimedia', 'MultimediaContent')
    MultimediaCategory = apps.get_model('multimedia', 'MultimediaCategory')

    MultimediaReview.objects.all().delete()
    AlbumMusic.objects.all().delete()
    MultimediaCategory.objects.all().delete()
    MultimediaContent.objects.all().delete()
    Category.objects.all().delete()
    Book.objects.all().delete()
    Music.objects.all().delete()
    Album.objects.all().delete()
    Multimedia.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0002_create_model'),
    ]

    operations = [
        migrations.RunPython(
            seed_multimedia,
            delete_multimedia,
        ),
    ]
