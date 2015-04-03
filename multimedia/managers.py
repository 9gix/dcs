from django.db import connection
from django.db import models
from django.core.urlresolvers import reverse

from .utils import (
    dictfetchall, dictfetchone
)


class BookManager(models.Manager):
    def all(self):
        books = []
        with connection.cursor() as c:
            c.execute('''
                SELECT m.id, m.name, description, isbn13, isbn10, price, o.name AS publisher
                FROM book, multimedia m, organisation o
                WHERE book.multimedia_id = m.id
                  AND m.organisation_id = o.id
            ''')

            for book in dictfetchall(c):
                books.append(book)

        for book in books:
            book['url'] = reverse('multimedia:book_detail', args=(book['isbn13'],))
        return books

    def get(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                SELECT m.id, m.name, description, isbn13, isbn10, price, o.name AS publisher
                FROM book, multimedia m, organisation o
                WHERE book.multimedia_id = m.id
                  AND m.organisation_id = o.id
                  AND book.isbn13 = %s
            ''', [kwargs['isbn13'], ])
            return dictfetchone(c)


class MusicManager(models.Manager):
    def all(self):
        items = []
        with connection.cursor() as c:
            c.execute('''
                SELECT
                  mul.id AS id,
                  mul.name AS name,
                  a.name AS album,
                  duration,
                  price,
                  o.name AS organisation
                FROM multimedia mul, music mus, album_music am, album a, organisation o
                WHERE mul.id = mus.multimedia_id
                  AND am.music_id = mus.multimedia_id
                  AND am.album_id = a.id
                  AND mul.organisation_id = o.id
            ''')

            for item in dictfetchall(c):
                items.append(item)

        for item in items:
            item['url'] = reverse('multimedia:music_detail', args=(item['id'],))

        return items

    def get(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                SELECT
                  mul.name AS name,
                  a.name AS album,
                  description,
                  duration,
                  price,
                  o.name AS organisation
                FROM multimedia mul, music mus, album_music am, album a, organisation o
                WHERE mul.id = mus.multimedia_id
                  AND am.music_id = mus.multimedia_id
                  AND am.album_id = a.id
                  AND mul.organisation_id = o.id
                  AND mul.id = %s;
            ''', [kwargs['id'], ])
            return dictfetchone(c)
