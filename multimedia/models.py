from django.db import connection
from django.db import models
from django.core.urlresolvers import reverse_lazy

dummy_book = {
    'isbn13': 9871234567890,
    'isbn10': 1234567890,
    'title': 'Hello World',
    'url': reverse_lazy('multimedia:book_detail', kwargs={'isbn13': 9871234567890,}),
    'description': '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Cras suscipit arcu sapien. Ut aliquet nisi est. 
    Duis vulputate erat arcu.

    Etiam vel ipsum quis est iaculis vehicula. 
    Fusce faucibus ipsum nec ligula tempor ultrices.
    Vestibulum tristique vitae risus lobortis volutpat.
    ''',
    'authors': [
        {
            'name': 'Foo',
            'url': '/book-authors/foo/',
        },
        {
            'name': 'Bar',
            'url': '/book-authors/bar/',
        },
    ],
    'publisher': {
        'name': 'Exclusive Gix',
        'url': '/book-publisher/exclusive-gix',
    },
}

class Multimedia(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField('Category')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'multimedia'


class BookManager(models.Manager):
    def all(self):
        return [dummy_book, dummy_book, dummy_book]

    def get(self, *args, **kwargs):
        return dummy_book

class Book(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    isbn13 = models.CharField(max_length=13)
    isbn10 = models.CharField(max_length=10)

    published_on = models.DateField()

    objects = BookManager()

    class Meta:
        managed = False
        db_table = 'book'



class Music(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'music'

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    musics = models.ManyToManyField('Music')

    class Meta:
        managed = False
        db_table = 'album'

class Application(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    version = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'application'

class Movie(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'movie'


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    parent = models.ForeignKey('self')

    class Meta:
        managed = False
        db_table = 'category'

