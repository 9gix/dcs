from django.db import connection
from django.db import models
from django.core.urlresolvers import reverse

from multimedia.utils import (
    dictfetchall, dictfetchone
)


class CartManager(models.Manager):
    def get(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                SELECT c.id, c.buyer_id, c.created_at, c.modified_at, 
                FROM cart c
                WHERE c.id = %s
            ''', [kwargs['id'], ])
        return dictfetchone(c)


class MultimediaManager(models.Manager):
    def get(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                SELECT m.name, m.price, sum(m.price) AS total_price
                FROM multimedia m
                WHERE m.id = %s
            ''', [kwargs['id'], ])
            return dictfetchone(c) 


"""
class CartItemManager(models.Model):
    def all(self, *args, **kwargs):
        items = []
        with connection.cursor() as c:
            c.execute('''
                SELECT ci.id, ci.multimedia_id, ci.object_type, ci.quantity
                FROM cart_item ci
                WHERE ci.cart_id = %s
            ''')

            for item in dictfetchall(c):
                items.append(item)

        for book??

        return items
        """