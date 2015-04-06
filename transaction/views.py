from django.shortcuts import render

from .models import (
	CartItem
)

from multimedia.models import Multimedia

# Create your views here.
def cart_item_list(request, cart_id):
	cart_items_raw = CartItem.objects.raw("""SELECT ci.id, ci.object_id, m.name, m.price
										 	 FROM cart_item ci, multimedia m 
										 	 WHERE ci.object_id = m.id AND
										 	   	   ci.cart_id = %s
									     """, [cart_id])
	cart_items = []
	total_price = 0
	for cart_item in cart_items_raw:
		item = {}
		item['id'] = cart_item.object_id
		item['name'] = cart_item.name
		item['price'] = cart_item.price
		total_price += cart_item.price
		cart_items.append(item)

	return render(request, '../templates/transaction/checkout.html', {'cart_items': cart_items, 'total_price': total_price})