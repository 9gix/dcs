from django.db import connection
from django.db import models
from multimedia.utils import (
    dictfetchall, dictfetchone
)

class MultimediaReviewManager(models.Manager):
    def filter(self, *args, **kwargs):
        reviews = []
        with connection.cursor() as c:
            c.execute('''
                SELECT
                  username,
                  rating,
                  comment,
                  created_at AS datetime
                FROM multimedia_review mr, auth_user u
                WHERE u.id = mr.user_id
                  AND multimedia_id = %s
            ''', [kwargs['multimedia_id'],])

            for review in dictfetchall(c):
                reviews.append(review)

        return reviews
