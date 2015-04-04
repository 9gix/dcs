from django.contrib import admin
from .models import (
        Cart, CartItem, Transaction
)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

    related_lookup_fields = {
        'generic': [['content_type', 'object_id'], ],
    }

class CartModelAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]



admin.site.register(Cart, CartModelAdmin)
admin.site.register(Transaction)
