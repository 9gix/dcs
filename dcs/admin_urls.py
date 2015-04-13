from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from .views import home

from multimedia import admin_urls

urlpatterns = [
    url(r'^', include(admin_urls.urlpatterns)),
]
