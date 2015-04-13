from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from multimedia.models import MULTIMEDIA_MODELS

class Crew(models.Model):
    content_type = models.ForeignKey(ContentType, limit_choices_to=MULTIMEDIA_MODELS)
    object_id = models.PositiveIntegerField()
    multimedia = GenericForeignKey('content_type', 'object_id')
    person = models.ForeignKey('Person')
    role = models.ForeignKey('Role')

    def __str__(self):
        return "{} as {} in {}".format(self.person, self.role, self.multimedia)


class Role(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "people"

    def __str__(self):
        return self.name
