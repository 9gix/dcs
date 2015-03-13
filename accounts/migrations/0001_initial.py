# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def insert_user(apps, schema_editor):
    call_command('loaddata', 'user_data', app_label='accounts')

def delete_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
            ('auth', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(
                insert_user,
                delete_user,
            ),
    ]
