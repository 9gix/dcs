from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db import connection
from django.contrib.contenttypes.models import ContentType

from multimedia.utils import dictfetchone

from .models import (
    CartItem, 
    Cart,
)

from multimedia.models import Multimedia

def cart_item_list(request):
    cart_id = __getUserCartId(request.user.id)

    if cart_id == -1:
        newCart = Cart(buyer=request.user)
        newCart.insert()
        cart_id = __getUserCartId(request.user.id)

    cart_items_raw = CartItem.objects.raw("""SELECT ci.id, ci.object_id, m.name, m.price
                                             FROM cart_item ci, multimedia m 
                                             WHERE ci.object_id = m.id AND
                                                   ci.cart_id = %s
                                         """, [cart_id])

    total_price_raw = CartItem.objects.raw("""SELECT ci.id, sum(m.price) as total
                                              FROM cart_item ci, multimedia m 
                                              WHERE ci.object_id = m.id AND
                                                    ci.cart_id = %s
                                           """, [cart_id])

    cart_items = []
    total_price = 0

    for entry in total_price_raw:
        total_price = entry.total

    for cart_item in cart_items_raw:
        item = {}
        item['id'] = cart_item.object_id
        item['name'] = cart_item.name
        item['price'] = cart_item.price
        cart_items.append(item)

    return render(request, 'transaction/checkout.html', {'cart_id': cart_id, 'cart_items': cart_items, 'total_price': total_price})

def cart_purchase(request):
    cart_id = request.POST['cart_id']
    user = request.user

    __updateStatus(cart_id)

    newCart = Cart(buyer=user)
    newCart.insert()

    new_cart_id = __getUserCartId(user.id)

    return redirect("carts:cart_item_list")

def cart_item_delete(request):
    cart_id = request.POST['cart_id']
    cart_item_id = request.POST['cart_item_id']

    __deleteItem(cart_id, cart_item_id)

    return redirect("carts:cart_item_list")

def cart_item_add(request, multimedia_id, multimedia_type):
    cart = Cart.objects.get(buyer=request.user)
    content_type = ContentType.objects.get_for_model(model=multimedia_type)
    GenericMultimedia = content_type.model_class()
    multimedia = GenericMultimedia.objects.get(id=multimedia_id)
    CartItem.objects.create(content_object=multimedia, cart=cart)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))