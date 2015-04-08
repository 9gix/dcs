from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('transaction.views',
	url(r'^purchase/', 'cart_purchase', name='cart_purchase'),
	url(r'^delete/', 'cart_item_delete', name='cart_item_delete'),
	url(r'^$', 'cart_item_list', name='cart_item_list'),
)
