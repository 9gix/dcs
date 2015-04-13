from django.db import models
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from multimedia.models import MULTIMEDIA_MODELS
from .managers import MultimediaReviewManager


class MultimediaReview(models.Model):
    comment = models.TextField(blank=True)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, limit_choices_to=MULTIMEDIA_MODELS)
    object_id = models.PositiveIntegerField()
    multimedia = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User)

    objects = MultimediaReviewManager()

    class Meta:
        managed = False
        db_table = 'multimedia_review'

    def __str__(self):
        return "Review {}".format(self.id)
