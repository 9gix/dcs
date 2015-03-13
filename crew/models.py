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

    def __str__(self):
        return "{} {} at {}".format(self.person, self.role, self.organisation)


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


class Organisation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'organisation'

    def __str__(self):
        return self.name
