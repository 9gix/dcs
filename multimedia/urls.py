from django.conf.urls import patterns, include, url
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^books/$', views.book_list,
        name='book_list'),
    url(r'^books/(?P<isbn13>\d{13})/', views.book_detail,
        name='book_detail'),

    url(r'^music/$', views.music_list,
        name='music_list'),
    url(r'^music/(?P<music_id>\d+)/', views.music_detail,
        name='music_detail'),

    url(r'^app/$', views.application_list,
        name='application_list'),
    url(r'^app/(?P<application_id>\d+)/', views.application_detail,
        name='application_detail'),

    url(r'^movie/$', views.movie_list,
        name='movie_list'),
    url(r'^movie/(?P<movie_id>\d+)/', views.movie_detail,
        name='movie_detail'),
]

