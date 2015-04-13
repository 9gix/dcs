from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from .views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nimda/', include('grappelli.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^carts/', include('transaction.urls', namespace='carts')),
    url(r'^review/', include('review.urls', namespace='review')),
    url(r'^', include('multimedia.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

