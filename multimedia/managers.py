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

