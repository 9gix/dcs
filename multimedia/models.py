from django.db import models, connection, transaction
from django.utils import timezone
from django.core.validators import MinLengthValidator

from imagekit.models import ImageSpecField
from pilkit import processors

from .managers import (
    BookManager,
    MusicManager,
    ApplicationManager,
    MovieManager,
    MultimediaCategoryManager,
)

class Organisation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'organisation'

    def __str__(self):
        return self.name

class Multimedia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField('Category', through='MultimediaCategory')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    organisation = models.ForeignKey('Organisation')

    class Meta:
        managed = False
        db_table = 'multimedia'

    def __str__(self):
        return self.name

class MultimediaImage(models.Model):
    caption = models.CharField(max_length=100, blank=True)
    original = models.ImageField(upload_to='original')
    multimedia = models.ForeignKey('Multimedia')
    thumb150x150 = ImageSpecField(source='original',
            processors=[processors.Thumbnail(150, 150)], format='JPEG')
    thumb250x250 = ImageSpecField(source='original',
            processors=[processors.ResizeToFit(250, 250)], format='JPEG')

    class Meta:
        managed = False
        db_table = 'multimedia_image'


class Book(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    isbn13 = models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    isbn10 = models.CharField(max_length=10, validators=[MinLengthValidator(10)])

    published_on = models.DateField()

    objects = BookManager()

    class Meta:
        managed = False
        db_table = 'book'

    @transaction.atomic
    def insert(self):
        with connection.cursor() as c:
            c.execute('''
                INSERT INTO multimedia
                  (name, description, price, organisation_id,
                    created_at, modified_at)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', [self.name, self.description, self.price, self.organisation_id,
                    timezone.now(), timezone.now()])

            mul_id = c.lastrowid
            self.multimedia = Multimedia.objects.get(id=mul_id)

            c.execute('''
                INSERT INTO book
                  (multimedia_id, isbn13, isbn10, published_on)
                VALUES (%s, %s, %s, %s)
            ''', [mul_id, self.isbn13, self.isbn10, self.published_on])


    @transaction.atomic
    def update(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                UPDATE multimedia
                SET
                  name = %s,
                  description = %s,
                  price = %s,
                  organisation_id = %s,
                  modified_at = %s
                WHERE id = %s
            ''', [self.name, self.description, self.price, self.organisation_id,
                    timezone.now(), kwargs['multimedia_id']])

            c.execute('''
                UPDATE book
                SET
                  isbn13 = %s,
                  isbn10 = %s,
                  published_on = %s
                WHERE multimedia_id = %s
            ''', [self.isbn13, self.isbn10, self.published_on,
                    kwargs['multimedia_id']])


class Movie(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    duration = models.IntegerField()

    objects = MovieManager()

    class Meta:
        managed = False
        db_table = 'movie'

class Application(Multimedia):
    multimedia = models.OneToOneField('Multimedia', parent_link=True)
    version = models.CharField(max_length = 10)

    objects = ApplicationManager()

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

    objects = MultimediaCategoryManager()

    class Meta:
        managed = False
        db_table = 'multimedia_category'
        verbose_name_plural = "multimedia categories"

    def __str__(self):
        return "{}{}".format(self.multimedia, self.category)

    def insert(self):
        with connection.cursor() as c:
            c.execute('''
                INSERT INTO multimedia_category
                  (multimedia_id, category_id)
                VALUES (%s, %s)
            ''', [self.multimedia_id, self.category_id])
