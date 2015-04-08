# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_create_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultimediaReview',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('comment', models.TextField(blank=True)),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'multimedia_review',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
