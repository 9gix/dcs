from django.db import connection
from django.db import models
from django.core.urlresolvers import reverse

from .utils import (
    dictfetchall, dictfetchone
)


class CartManager(models.Model):
    def get(self, *args, **kwargs):
        with connection.cursor() as c:
            c.execute('''
                SELECT c.id, c.buyer_id, c.created_at, c.modified_at, 
                FROM cart c
                WHERE c.id = %s
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