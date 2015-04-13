from django.db import connection
from django.db import models
from django.core.urlresolvers import reverse

from .utils import (
    dictfetchall, dictfetchone
)

class MovieManager(models.Manager):
    def all(self):
        movies = []
        with connection.cursor() as c:
            c.execute('''
                SELECT m.id, m.name, description, duration, price, o.name AS studio
                FROM movie mo, multimedia m, organisation o
                WHERE mo.multimedia_id = m.id
                  AND m.organisation_id = o.id
            ''')

            for movie in dictfetchall(c):
                movies.append(movie)

        for movie in movies:
            movie['url'] = reverse('multimedia:movie_detail', args=(movie['id'],))
        return movies

    def get(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                SELECT 
                  m.id, 
                  m.name, 
                  description,
                  duration,  
                  price, 
                  o.name AS studio
                FROM 
                  movie mo, 
                  multimedia m, 
                  organisation o
                WHERE mo.multimedia_id = m.id
                  AND m.organisation_id = o.id
                  AND m.id = %s
            ''', [kwargs['id'], ])
            return dictfetchone(c)

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
            book['url'] = reverse('multimedia:book_detail', args=(book['id'],))
        return books

    def get(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                SELECT m.id, m.name, description, isbn13, isbn10, price,
                  m.organisation_id AS organisation, o.name AS publisher, published_on
                FROM book, multimedia m, organisation o
                WHERE book.multimedia_id = m.id
                  AND m.organisation_id = o.id
                  AND book.multimedia_id = %s
            ''', [kwargs['id']])
            return dictfetchone(c)

    def delete(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                DELETE FROM multimedia
                WHERE id = %s
            ''', [kwargs['id'], ])

class MusicManager(models.Manager):
    def all(self):
        items = []
        with connection.cursor() as c:
            c.execute('''
                SELECT
                  mul.id AS id,
                  mul.name AS name,
                  a.name AS album,
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
            'app' AS url_prefix,
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

    QUERY_TABLE = {
        'application': APPLICATION_QUERY,
        'book': BOOK_QUERY,
        'movie': MOVIE_QUERY,
        'music': MUSIC_QUERY
    }

    def __get_whole_query(self, multimedia_type, **kwargs):
        substitutes = {}

        keywords = kwargs.get('keywords')
        if keywords:
            title_clause = self.__generate_title_clause(keywords)
            desc_clause = self.__generate_description_clause(keywords)
            crew_clause = self.__generate_crew_clause(keywords)
            clauses = {
                'title': title_clause[0],
                'desc': desc_clause[0],
                'crew': crew_clause[0],
            }
            cond_query = " AND ({title} OR {desc} OR {crew})".format(**clauses)

            substitutes = self.__merge_dicts(substitutes, title_clause[1])
            substitutes = self.__merge_dicts(substitutes, desc_clause[1])
            substitutes = self.__merge_dicts(substitutes, crew_clause[1])
        else:
            cond_query = ""


        category = kwargs.get('category')
        if category:
            clause = self.__generate_category_clause(category)
            cat_query = " AND {}".format(clause[0])
            substitutes = self.__merge_dicts(substitutes, clause[1])
        else:
            cat_query = ""

        query = "{} {} {}".format(
                self.QUERY_TABLE.get(multimedia_type, ''),
                cond_query,
                cat_query)

        return (query, substitutes)

    def __generate_title_clause(self, keywords):
        split_keywords = keywords.split()
        clauses = []
        connector = " AND "
        substitutes = {}

        for i, keyword in enumerate(split_keywords):
            clauses.append("m.name LIKE %(keyword{})s".format(i))
            substitutes["keyword{}".format(i)] = '%{}%'.format(keyword)

        return (connector.join(clauses), substitutes)

    def __generate_description_clause(self, keywords):
        split_keywords = keywords.split()
        clauses = []
        connector = " AND "
        substitutes = {}

        for i, keyword in enumerate(split_keywords):
            clauses.append("m.description LIKE %(keyword{})s".format(i))
            substitutes["keyword{}".format(i)] = '%{}%'.format(keyword)

        return (connector.join(clauses), substitutes)

    def __generate_crew_clause(self, keywords):
        split_keywords = keywords.split()
        clause = '''
            m.id IN (SELECT c.multimedia_id FROM
            crew c, person p
            WHERE c.person_id = p.id
        '''
        substitutes = {}

        for i, keyword in enumerate(split_keywords):
            clause += "AND p.name LIKE %(keyword{})s".format(i)
            substitutes["keyword{}".format(i)] = '%{}%'.format(keyword)
        clause += ")"

        return (clause, substitutes)

    def __generate_category_clause(self, category):
        clause = '''
            m.id IN (SELECT m.multimedia_id FROM
            multimedia_category m, category c
            WHERE m.category_id = c.id
            AND c.name LIKE %(category)s)
        '''
        substitutes = {"category": '%{}%'.format(category)};
        return (clause, substitutes)

    def __merge_dicts(self, x, y):
        z = x.copy()
        z.update(y)
        return z


    def search(self, multimedia_types, **kwargs):
        if len(multimedia_types) == 0:
            multimedia_types = ['application', 'movie', 'book', 'music']
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

class MultimediaCategoryManager(models.Manager):
    def filter(self, *args, **kwargs):
        result = []
        with connection.cursor() as c:
            c.execute('''
                SELECT * FROM multimedia_category
                WHERE multimedia_id = %s
            ''', [kwargs['multimedia_id']])

            for category in dictfetchall(c):
                result.append(category)

        return result

    def delete(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                DELETE FROM multimedia_category
                WHERE multimedia_id = %s
            ''', [kwargs['multimedia_id']])
