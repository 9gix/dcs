from django.shortcuts import render

from .models import (
	CartItem
)

from multimedia.models import Multimedia

# Create your views here.
def cart_item_list(request, cart_id):
	cart_items_query_set = CartItem.objects.filter(cart=cart_id)
	cart_items_dict = cart_items_query_set.values()
	total_price = 0;

	for item in cart_items_dict:
		multimedia = Multimedia.objects.get(id=item['object_id'])
		item['name'] = multimedia.name
		item['price'] = multimedia.price
		item['total'] = item['quantity'] * multimedia.price
		total_price += item['total']

	return render(request, '../templates/transaction/checkout.html', {'cart_items': cart_items_dict, 'total_price': total_price})