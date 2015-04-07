# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

with open('schema/create_multimedia_review.sql') as f:
    create_review_script = f.read()

with open('schema/drop_multimedia_review.sql') as f:
    drop_review_script = f.read()

class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_create_table'),
    ]

    operations = [
        migrations.RunSQL(
            create_review_script,
            drop_review_script
        )
    ]
