from django.db import models
from django.db import connection

class MultimediaReview(models.Model):
    id = models.AutoField(primary_key=True)
    multimedia = models.ForeignKey('multimedia.Multimedia')
    comment = models.TextField(blank=True)
    rating = models.IntegerField()

    def __init__(self, multimedia_id, comment, rating):
        self.multimedia = multimedia_id
        self.comment = comment
        self.rating = rating

    class Meta:
        managed = False
        db_table = 'multimedia_review'

    def save(self):
        with connection.cursor() as c:
            c.execute('''
                INSERT INTO multimedia_review
                  (multimedia_id, comment, rating)
                VALUES (%s, %s, %s)
            ''', [self.multimedia_id, self.comment, self.rating])

    def __str__(self):
        return "Review {}".format(self.id)
