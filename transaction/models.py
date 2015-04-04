from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

import multimedia

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cart'

    def __str__(self):
        import ipdb; ipdb.set_trace()
        return self.buyer.username

class CartItem(models.Model):
    cart = models.ForeignKey('Cart')
    quantity = models.IntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    class Meta:
        db_table = 'cart_item'

    #def __str__(self):
    #    return self.content_object

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey('Cart')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'transaction'



