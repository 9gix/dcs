from django.db import models
from .managers import CrewManager

class Crew(models.Model):
    id = models.AutoField(primary_key=True)
    multimedia = models.ForeignKey('multimedia.Multimedia')
    person = models.ForeignKey('Person')
    role = models.ForeignKey('Role')

    objects = CrewManager()

    class Meta:
        managed = False
        db_table = 'crew'

    def __str__(self):
        return "{} as {} in {}".format(self.person, self.role, self.multimedia)


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'role'

    def __str__(self):
        return self.name


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'person'
        verbose_name_plural = "people"

    def __str__(self):
        return self.name


