from django.db import connection
from django.db import models


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


class Book(Multimedia):
    isbn13 = models.CharField(max_length=13)
    isbn10 = models.CharField(max_length=10)

    published_on = models.DateField()

    class Meta:
        managed = False
        db_table = 'book'


class Music(Multimedia):
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
    version = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'application'

class Movie(Multimedia):
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

