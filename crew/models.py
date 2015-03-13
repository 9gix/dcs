from django.db import models


class Crew(models.Model):
    id = models.AutoField(primary_key=True)
    multimedia = models.ForeignKey('multimedia.Multimedia')
    person = models.ForeignKey('Person')
    role = models.ForeignKey('Role')
    organisation = models.ForeignKey('Organisation')

    class Meta:
        managed = False
        db_table = 'crew'


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'role'

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'person'
        verbose_name_plural = "people"

class Organisation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'organisation'
