# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

with open('schema/create_multimedia.sql') as f:
    create_multimedia_script = f.read()

with open('schema/drop_multimedia.sql') as f:
    drop_multimedia_script = f.read()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            create_multimedia_script,
            drop_multimedia_script,
        ),
    ]
