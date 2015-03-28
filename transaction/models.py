from django.db import models
from django.contrib.auth.models import User

import multimedia

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cart'


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey('Cart')
    object = models.ForeignKey(multimedia.models.Multimedia)
    object_type = models.CharField(max_length=45)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cart_item'


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey('Cart')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'transaction'



