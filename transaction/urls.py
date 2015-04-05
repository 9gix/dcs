from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('transaction.views',
	url(r'^(?P<cart_id>\d+)/', 'cart_item_list', name='cart_item_list'),
)
