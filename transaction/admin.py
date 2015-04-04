from django.contrib import admin
from django.contrib.contenttypes import admin as ct_admin
from .models import (
        Cart, CartItem, Transaction
)

class CartItemModelAdmin(ct_admin.GenericTabularInline):
	model = CartItem

class CartModelAdmin(admin.ModelAdmin):
	inlines = [CartItemModelAdmin]

admin.site.register(Cart, CartModelAdmin)
admin.site.register(CartItem)
admin.site.register(Transaction)
