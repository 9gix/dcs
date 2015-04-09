from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render

from . import views

def crud_urls(obj):
    return [
        url(r'^$', obj.list_view, name='index'),
        url(r'^add/', obj.add_view, name='add'),
        url(r'^(?P<pk>\d+)/', obj.detail_view, name='detail'),
        url(r'^(?P<pk>\d+)/edit/', obj.edit_view, name='edit'),
        url(r'^(?P<pk>\d+)/delete/', obj.delete_view, name='delete'),
    ]

class CRUDViewSet(object):
    def list_view(self, request, *args, **kwargs):
        return render(request, 'multimedia/admin/index.html')
    def add_view(self, request, *args, **kwargs):
        return render(request, 'multimedia/admin/add.html')
    def edit_view(self, request, *args, **kwargs):
        return render(request, 'multimedia/admin/edit.html')
    def delete_view(self, request, *args, **kwargs):
        return render(request, 'multimedia/admin/delete.html')
    def detail_view(self, request, *args, **kwargs):
        return render(request, 'multimedia/admin/detail.html')

class BookCRUDViewSet(CRUDViewSet):
    pass
class MovieCRUDViewSet(CRUDViewSet):
    pass
class MusicCRUDViewSet(CRUDViewSet):
    pass
class AppCRUDViewSet(CRUDViewSet):
    pass


urlpatterns = [
    url(r'^books/', include((crud_urls(BookCRUDViewSet()), 'multimedia', 'book'))),
    url(r'^movies/', include((crud_urls(MovieCRUDViewSet()), 'multimedia', 'movie'))),
    url(r'^music/', include((crud_urls(MusicCRUDViewSet), 'multimedia', 'music'))),
    url(r'^apps/', include((crud_urls(AppCRUDViewSet()), 'multimedia', 'app'))),
]
