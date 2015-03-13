# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

with open('schema/create_crew.sql') as f:
    create_crew_script = f.read()

with open('schema/drop_crew.sql') as f:
    drop_crew_script = f.read()

class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_create_table'),
    ]

    operations = [
        migrations.RunSQL(
            create_crew_script,
            drop_crew_script
        )
    ]
