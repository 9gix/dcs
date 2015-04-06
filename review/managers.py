from django.db import connection
from django.db import models
from multimedia.utils import (
    dictfetchall, dictfetchone
)

class MultimediaReviewManager(models.Model):
    def filter(self, *args, **kwargs):
        reviews = []
        with connection.cursor() as c:
            c.execute('''
                SELECT * FROM multimedia_review
                WHERE multimedia_id = %s
            ''', [kwargs['multimedia_id'],])

        for review in dictfetchall(c):
            reviews.append(review)

        return reviews
