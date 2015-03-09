from django.db import connection
from django.db import models


class Multimedia(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField('Category')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Book(Multimedia):
    isbn13 = models.CharField(max_length=13)
    isbn10 = models.CharField(max_length=10)

    published_on = models.DateField()


class Music(Multimedia):
    duration = models.IntegerField()

class Album(models.Model):
    name = models.CharField(max_length=45)
    musics = models.ManyToManyField('Music')

class Application(Multimedia):
    version = models.CharField(max_length=10)

class Movie(Multimedia):
    duration = models.IntegerField()



# CREW MODEL

class Crew(models.Model):
    multimedia = models.ForeignKey('Multimedia')
    person = models.ForeignKey('Person')
    role = models.ForeignKey('Role')
    organization = models.ForeignKey('Organization')


class Role(models.Model):
    name = models.CharField(max_length=45)

class Person(models.Model):
    name = models.CharField(max_length=45)

class Organization(models.Model):
    name = models.CharField(max_length=45)


# Category
class Category(models.Model):
    name = models.CharField(max_length=45)
    parent = models.ForeignKey('self')
