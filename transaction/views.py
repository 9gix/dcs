from django.shortcuts import render

# Create your views here.
def cart_item_list(request, cart_id):
	return render(request, '../templates/transaction/checkout.html')