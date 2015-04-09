from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from .views import home

urlpatterns = [
    url(r'^', include('multimedia.admin_urls', namespace='multimedia')),
]
