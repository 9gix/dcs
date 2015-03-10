# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

create_multimedia_table = """
CREATE TABLE multimedia (
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL NULL,
    created_at DATETIME NOT NULL,
    modified_at DATETIME NOT NULL,
    PRIMARY KEY (id)
);
"""

delete_multimedia_table = """
DROP TABLE multimedia;
"""

create_book_table = """
CREATE TABLE book (
    id INT NOT NULL,
    multimedia_id INT NOT NULL,
    isbn13 CHAR(13) NULL,
    isbn10 CHAR(10) NULL,
    published_on DATE NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_book_multimedia
        FOREIGN KEY (multimedia_id)
        REFERENCES multimedia (id)
);
"""

delete_book_table = """
DROP TABLE book;
"""

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            create_multimedia_table,
            delete_multimedia_table,
        ),
        migrations.RunSQL(
            create_book_table,
            delete_book_table,
        ),
    ]
