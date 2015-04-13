from django.db import models, connection
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from multimedia.models import MULTIMEDIA_MODELS


class Cart(models.Model):
    buyer = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        shopping_list = "Total Quantity: {}".format(
                self.cartitem_set.aggregate(Count('id'))['id__count'])
        return "{} - ({})".format(self.buyer.username, shopping_list)


class CartItem(models.Model):

    cart = models.ForeignKey('Cart')
    content_type = models.ForeignKey(ContentType,
            limit_choices_to=MULTIMEDIA_MODELS)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __str__(self):
        return str(self.content_object)
