from django.db import models

from .managers import (
    BookManager,
    MusicManager,
)


class Multimedia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField('Category', through='MultimediaCategory')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'multimedia'

    def __str__(self):
        return self.name


class Book(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    isbn13 = models.CharField(max_length=13)
    isbn10 = models.CharField(max_length=10)

    published_on = models.DateField()

    objects = BookManager()

    class Meta:
        managed = False
        db_table = 'book'

class Movie(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'movie'

class Application(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    version = models.CharField(max_length = 10)

    class Meta:
        managed = False
        db_table = 'application'


class Music(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    duration = models.IntegerField(null=True);

    objects = MusicManager()

    class Meta:
        managed = False
        db_table = 'music'


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    musics = models.ManyToManyField('Music', 
        through='AlbumMusic')

    class Meta:
        managed = False
        db_table = 'album'

    def __str__(self):
        return self.name


class AlbumMusic(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey('Album')
    music = models.ForeignKey('Music')

    class Meta:
        managed = False
        db_table = 'album_music'

    def __str__(self):
        return "{} - {}".format(self.album, self.music)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    parent_category = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name_plural = "categories"

    def __str__(self):
        if self.parent_category:
            return "{} -> {}".format(self.parent_category, self.name)
        else:
            return self.name

class MultimediaCategory(models.Model):
    id = models.AutoField(primary_key=True)
    multimedia = models.ForeignKey('Multimedia')
    category = models.ForeignKey('Category')

    class Meta:
        managed = False
        db_table = 'multimedia_category'
        verbose_name_plural = "multimedia categories"

    def __str__(self):
        return "{}{}".format(self.multimedia, self.category)


class MultimediaContent(models.Model):
    id = models.AutoField(primary_key=True)
    multimedia = models.ForeignKey('Multimedia')
    caption = models.CharField(max_length=128)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'multimedia_content'

    def __str__(self):
        return self.caption


class MultimediaReview(models.Model):
    id = models.AutoField(primary_key=True)
    multimedia = models.ForeignKey('Multimedia')
    comment = models.TextField(blank=True)
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'multimedia_review'


    def __str__(self):
        return "Review {}".format(self.id)
