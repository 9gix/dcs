from django.db import models
from django.db import connection
from django.contrib.auth.models import User
from .managers import MultimediaReviewManager

class MultimediaReview(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    multimedia = models.ForeignKey('multimedia.Multimedia')
    user = models.ForeignKey(User)

    objects = MultimediaReviewManager()

    class Meta:
        managed = False
        db_table = 'multimedia_review'

    def insert(self):
        with connection.cursor() as c:
            c.execute('''
                INSERT INTO multimedia_review
                  (multimedia_id, user_id, comment, rating)
                VALUES (%s, %s, %s, %s)
            ''', [self.multimedia_id, self.user_id, self.comment, self.rating])

    def __str__(self):
        return "Review {}".format(self.id)
