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
                'managed': False,
                'db_table': 'album',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlbumMusic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'managed': False,
                'db_table': 'album_music',
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
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'managed': False,
                'db_table': 'multimedia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('multimedia', models.OneToOneField(to='multimedia.Multimedia', serialize=False, parent_link=True, primary_key=True)),
                ('duration', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'movie',
            },
            bases=('multimedia.multimedia',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('multimedia', models.OneToOneField(to='multimedia.Multimedia', serialize=False, parent_link=True, primary_key=True)),
                ('isbn13', models.CharField(max_length=13)),
                ('isbn10', models.CharField(max_length=10)),
                ('published_on', models.DateField()),
            ],
            options={
                'managed': False,
                'db_table': 'book',
            },
            bases=('multimedia.multimedia',),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('multimedia', models.OneToOneField(to='multimedia.Multimedia', serialize=False, parent_link=True, primary_key=True)),
                ('version', models.CharField(max_length=10)),
            ],
            options={
                'managed': False,
                'db_table': 'application',
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
            name='Music',
            fields=[
                ('multimedia', models.OneToOneField(to='multimedia.Multimedia', serialize=False, parent_link=True, primary_key=True)),
                ('duration', models.IntegerField(null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'music',
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
                'managed': False,
                'db_table': 'organisation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MultimediaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('caption', models.CharField(max_length=100, blank=True)),
                ('original', models.ImageField(upload_to='original')),
                ('multimedia', models.ForeignKey(to='multimedia.Multimedia')),
            ],
            options={
                'managed': False,
                'db_table': 'multimedia_image',
            },
            bases=(models.Model,),
        ),
    ]
