# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_create_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'album',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlbumMusic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'album_music',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'db_table': 'category',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'multimedia',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('multimedia', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='multimedia.Multimedia')),
                ('duration', models.IntegerField()),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
            bases=('multimedia.multimedia',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('multimedia', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='multimedia.Multimedia')),
                ('isbn13', models.CharField(max_length=13)),
                ('isbn10', models.CharField(max_length=10)),
                ('published_on', models.DateField()),
            ],
            options={
                'db_table': 'book',
                'managed': False,
            },
            bases=('multimedia.multimedia',),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('multimedia', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='multimedia.Multimedia')),
                ('version', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'application',
                'managed': False,
            },
            bases=('multimedia.multimedia',),
        ),
        migrations.CreateModel(
            name='MultimediaCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'multimedia categories',
                'db_table': 'multimedia_category',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MultimediaContent',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('caption', models.CharField(max_length=128)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'multimedia_content',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MultimediaReview',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('comment', models.TextField(blank=True)),
                ('rating', models.IntegerField()),
            ],
            options={
                'db_table': 'multimedia_review',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('multimedia', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='multimedia.Multimedia')),
                ('duration', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'music',
                'managed': False,
            },
            bases=('multimedia.multimedia',),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'organisation',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
