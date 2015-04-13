from django.conf.urls import patterns, include, url
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^books/', include([
            url(r'^$', views.book_list,
                name='list'),
            url(r'^(?P<pk>\d+)/$', views.book_detail,
                name='detail'),
        ], 'multimedia', 'book')
    ),
    url(r'^music/', include([
            url(r'^$', views.music_list,
                name='list'),
            url(r'^(?P<pk>\d+)/$', views.music_detail,
                name='detail'),
        ], 'multimedia', 'music')
    ),
    url(r'^app/', include([
            url(r'^$', views.application_list,
                name='list'),
            url(r'^(?P<pk>\d+)/$', views.application_detail,
                name='detail'),
        ], 'multimedia', 'app')
    ),
    url(r'^movie/', include([        
        url(r'^$', views.movie_list,
            name='list'),
        url(r'^(?P<pk>\d+)/$', views.movie_detail,
            name='detail'),
        ], 'multimedia', 'movie')
    ),

    url(r'^search/', views.search_result, name='search_result'),
    url(r'^advanced_search/', views.advanced_search, name='advanced_search')
]
