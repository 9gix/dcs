from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^purchase/', views.cart_purchase, name='cart_purchase'),
    url(r'^delete/', views.cart_item_delete, name='cart_item_delete'),
    url(r'^$', views.cart_item_list, name='cart_item_list'),
    url(r'^(?P<multimedia_type>\w+)/(?P<multimedia_id>\d+)', views.cart_item_add, name='cart_item_add'),
]
