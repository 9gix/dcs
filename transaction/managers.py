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
                SELECT buyer_id
                FROM cart
                WHERE id = %s
            ''', [kwargs['cart_id'], ])
            return dictfetchone(c)