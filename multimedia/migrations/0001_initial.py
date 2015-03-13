# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

with open('schema/create_multimedia.sql') as f:
    create_multimedia_script = f.read()

with open('schema/drop_multimedia.sql') as f:
    drop_multimedia_script = f.read()

with open('schema/create_album.sql') as f:
    create_album_script = f.read()

with open('schema/drop_album.sql') as f:
    drop_album_script = f.read()

with open('schema/create_music.sql') as f:
    create_music_script = f.read()

with open('schema/drop_music.sql') as f:
    drop_music_script = f.read()

with open('schema/create_album_music.sql') as f:
    create_album_music_script = f.read()

with open('schema/drop_album_music.sql') as f:
    drop_album_music_script = f.read()

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            create_multimedia_script,
            drop_multimedia_script,
        ),
        migrations.RunSQL(
            create_album_script,
            drop_album_script,
        ),
        migrations.RUNSQL(
            create_music_script,
            drop_music_script,
        ),
        migrations.RUNSQL(
            create_album_music_script,
            drop_album_music_script,
        )
    ]
