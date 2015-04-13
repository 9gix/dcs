from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import admin_views as views

urlpatterns = [
    url(r'^books/',
        include([
            url(r'^$',
                views.ListBookView.as_view(), name='index'),
            url(r'^add/',
                views.AddBookView.as_view(), name='add'),
            url(r'^(?P<pk>\d+)/edit/',
                views.EditBookView.as_view(), name='edit'),
            url(r'^(?P<pk>\d+)/delete/',
                views.DeleteBookView.as_view(), name='delete'),
        ], 'multimedia', 'book')),

    url(r'^movies/',
        include([], 'multimedia', 'movie')),
    url(r'^music/',
        include([], 'multimedia', 'music')),
    url(r'^apps/',
        include([], 'multimedia', 'app')),
]
