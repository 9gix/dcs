from django.db import models, transaction
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from imagekit.models import ImageSpecField
from pilkit import processors

MULTIMEDIA_MODELS = (
    models.Q(app_label='multimedia', model='Book') | 
    models.Q(app_label='multimedia', model='Movie') | 
    models.Q(app_label='multimedia', model='Music') | 
    models.Q(app_label='multimedia', model='Application')
)

class Organisation(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Multimedia(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    organisation = models.ForeignKey('Organisation')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class MultimediaImage(models.Model):
    caption = models.CharField(max_length=100, blank=True)
    original = models.ImageField(upload_to='original')
    content_type = models.ForeignKey(ContentType, limit_choices_to=MULTIMEDIA_MODELS)
    object_id = models.PositiveIntegerField()
    multimedia = GenericForeignKey('content_type', 'object_id')
    thumb150x150 = ImageSpecField(source='original',
            processors=[processors.Thumbnail(150, 150)], format='JPEG')
    thumb250x250 = ImageSpecField(source='original',
            processors=[processors.ResizeToFit(250, 250)], format='JPEG')


class Book(Multimedia):
    isbn13 = models.CharField(max_length=13, validators=[MinLengthValidator(13)])
    isbn10 = models.CharField(max_length=10, validators=[MinLengthValidator(10)])

    published_on = models.DateField()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('book:detail', args=(self.pk,))

class Movie(Multimedia):
    duration = models.IntegerField()


class Application(Multimedia):
    version = models.CharField(max_length = 10)


class Music(Multimedia):
    duration = models.IntegerField(null=True);


class Album(models.Model):
    name = models.CharField(max_length=45)
    musics = models.ManyToManyField('Music',
        through='AlbumMusic')

    def __str__(self):
        return self.name


class AlbumMusic(models.Model):
    album = models.ForeignKey('Album')
    music = models.ForeignKey('Music')

    def __str__(self):
        return "{} - {}".format(self.album, self.music)


class Category(models.Model):
    name = models.CharField(max_length=45)
    parent_category = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        if self.parent_category:
            return "{} -> {}".format(self.parent_category, self.name)
        else:
            return self.name

class MultimediaCategory(models.Model):
    content_type = models.ForeignKey(ContentType, limit_choices_to=MULTIMEDIA_MODELS)
    object_id = models.PositiveIntegerField()
    multimedia = GenericForeignKey('content_type', 'object_id')

    category = models.ForeignKey('Category')

    class Meta:
        verbose_name_plural = "multimedia categories"

    def __str__(self):
        return "{} in {}".format(self.multimedia, self.category)
