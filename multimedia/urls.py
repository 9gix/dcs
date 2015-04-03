from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('multimedia.views',
    url(r'^books/$', 'book_list', name='book_list'),
    url(r'^books/(?P<isbn13>\d{13})/', 'book_detail', name='book_detail'),
    url(r'^music/$', 'music_list', name='music_list'),
    url(r'^music/(?P<music_id>\d+)/', 'music_detail', name='music_detail'),
)
