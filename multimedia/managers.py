from django.db import connection
from django.db import models
from django.core.urlresolvers import reverse

from .utils import (
    dictfetchall, dictfetchone
)

class ApplicationManager(models.Manager):
    def all(self):
        applications = []
        with connection.cursor() as c:
            c.execute('''
                SELECT m.id, m.name, description, version, price, o.name AS developer
                FROM application a, multimedia m, organisation o
                WHERE a.multimedia_id = m.id
                  AND m.organisation_id = o.id
            ''')

            for application in dictfetchall(c):
                applications.append(application)

        for application in applications:
            application['url'] = reverse('multimedia:application_detail', args=(application['id'],))
        return applications

    def get(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                SELECT 
                  m.id, 
                  m.name, 
                  description, 
                  version, 
                  price, 
                  o.name AS developer
                FROM 
                  application a, 
                  multimedia m, 
                  organisation o
                WHERE a.multimedia_id = m.id
                  AND m.organisation_id = o.id
                  AND m.id = %s
            ''', [kwargs['id'], ])
            return dictfetchone(c)

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
                  mul.id AS id,
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

class MultimediaManager(models.Manager):

    BOOK_QUERY = '''
        SELECT
            m.id AS id,
            m.name AS name,
            m.description AS description,
            m.price AS price,
            'books' AS url_prefix,
            b.isbn13 AS url_suffix
        FROM multimedia m, book b
        WHERE m.id = b.multimedia_id
    '''

    MUSIC_QUERY = '''
        SELECT
            m.id AS id,
            m.name AS name,
            m.description AS description,
            m.price AS price,
            'music' AS url_prefix,
            m.id AS url_suffix
        FROM multimedia m, music mus
        WHERE m.id = mus.multimedia_id
    '''

    APPLICATION_QUERY = '''
        SELECT
            m.id AS id,
            m.name AS name,
            m.description AS description,
            m.price AS price,
            'application' AS url_prefix,
            m.id AS url_suffix
        FROM multimedia m, application a
        WHERE m.id = a.multimedia_id
    '''

    MOVIE_QUERY = '''
        SELECT
            m.id AS id,
            m.name AS name,
            m.description AS description,
            m.price AS price,
            'movie' AS url_prefix,
            m.id AS url_suffix
        FROM multimedia m, movie mov
        WHERE m.id = mov.multimedia_id
    '''

    def __get_whole_query(self, multimedia_type, **kwargs):
        query = ""
        substitutes = {}
        if (multimedia_type == "application"):
            query = self.APPLICATION_QUERY
        elif (multimedia_type == "book"):
            query = self.BOOK_QUERY
        elif (multimedia_type == "movie"):
            query = self.MOVIE_QUERY
        elif (multimedia_type == "music"):
            query = self.MUSIC_QUERY

        if ('keywords' in kwargs):
            clause = self.__generate_title_clause(kwargs['keywords'])
            query += " AND (" + clause[0]
            substitutes = self.__merge_dicts(substitutes, clause[1])
            clause = self.__generate_description_clause(kwargs['keywords'])
            query += " OR " + clause[0]
            substitutes = self.__merge_dicts(substitutes, clause[1])
            clause = self.__generate_crew_clause(kwargs['keywords'])
            query += " OR " + clause[0] + ")"
            substitutes = self.__merge_dicts(substitutes, clause[1])

        return (query, substitutes)

    def __generate_title_clause(self, keywords):
        split_keywords = keywords.split(" ")
        clauses = []
        for i in range(0, len(split_keywords)):
            clauses.append("m.name LIKE %(keyword" + str(i) + ")s")
        connector = " AND "
        substitutes = {}

        for i in range(0, len(split_keywords)):
            substitutes["keyword" + str(i)] = '%' + split_keywords[i] + '%'

        return (connector.join(clauses), substitutes)

    def __generate_description_clause(self, keywords):
        split_keywords = keywords.split(" ")
        clauses = []
        for i in range(0, len(split_keywords)):
            clauses.append("m.description LIKE %(keyword" + str(i) + ")s")
        connector = " AND "
        substitutes = {}

        for i in range(0, len(split_keywords)):
            substitutes["keyword" + str(i)] = '%' + split_keywords[i] + '%'

        return (connector.join(clauses), substitutes)

    def __generate_crew_clause(self, keywords):
        split_keywords = keywords.split(" ")
        clauses = []
        clause = '''
            m.id IN (SELECT c.multimedia_id FROM
            crew c, person p
            WHERE c.person_id = p.id
        '''
        for i in range(0, len(split_keywords)):
            clause += "AND p.name LIKE %(keyword" + str(i) + ")s"
        clause += ")"
        substitutes = {}
        for i in range(0, len(split_keywords)):
            substitutes["keyword" + str(i)] = '%' + split_keywords[i] + '%'

        return (clause, substitutes)
    def __merge_dicts(self, x, y):
        z = x.copy()
        z.update(y)
        return z


    def search(self, multimedia_types=['application', 'movie', 'book', 'music'], **kwargs):
        clauses = []
        for mul_type in multimedia_types:
            clauses.append(self.__get_whole_query(mul_type, **kwargs))
        queries = []
        for clause in clauses:
            queries.append(clause[0])
        substitutes = {}
        for clause in clauses:
            substitutes = self.__merge_dicts(substitutes, clause[1])

        query = " UNION ".join(queries)

        items = []
        with connection.cursor() as c:
            c.execute(query, substitutes)
            for item in  dictfetchall(c):
                items.append(item)
        return items
