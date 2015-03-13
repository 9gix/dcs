# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def seed_crew(apps, schema_editor):
    call_command('loaddata', 'crew_data', app_label='crew')

def delete_crew(apps, schema_editor):
    Crew = apps.get_model('crew', 'Crew')
    Person = apps.get_model('crew', 'Person')
    Organisation = apps.get_model('crew', 'Organisation')
    Role = apps.get_model('crew', 'Role')

    Crew.objects.all().delete()
    Person.objects.all().delete()
    Organisation.objects.all().delete()
    Role.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('crew', '0002_create_model'),
        ('multimedia', '0003_seed_multimedia'),
    ]

    operations = [
        migrations.RunPython(
            seed_crew,
            delete_crew,
        ),
    ]
