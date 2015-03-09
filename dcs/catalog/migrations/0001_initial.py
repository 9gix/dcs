# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('parent', models.ForeignKey(to='catalog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('multimedia_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='catalog.Multimedia')),
                ('duration', models.IntegerField()),
            ],
            options={
            },
            bases=('catalog.multimedia',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('multimedia_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='catalog.Multimedia')),
                ('isbn13', models.CharField(max_length=13)),
                ('isbn10', models.CharField(max_length=10)),
                ('published_on', models.DateField()),
            ],
            options={
            },
            bases=('catalog.multimedia',),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('multimedia_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='catalog.Multimedia')),
                ('version', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=('catalog.multimedia',),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('multimedia_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='catalog.Multimedia')),
                ('duration', models.IntegerField()),
            ],
            options={
            },
            bases=('catalog.multimedia',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='multimedia',
            name='categories',
            field=models.ManyToManyField(to='catalog.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crew',
            name='multimedia',
            field=models.ForeignKey(to='catalog.Multimedia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crew',
            name='organization',
            field=models.ForeignKey(to='catalog.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crew',
            name='person',
            field=models.ForeignKey(to='catalog.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='crew',
            name='role',
            field=models.ForeignKey(to='catalog.Role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='musics',
            field=models.ManyToManyField(to='catalog.Music'),
            preserve_default=True,
        ),
    ]
