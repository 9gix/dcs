# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

with open('schema/create_transaction.sql') as f:
    create_transaction_script = f.read()

with open('schema/drop_transaction.sql') as f:
    drop_transaction_script = f.read()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            create_transaction_script,
            drop_transaction_script,
        ),
    ]
