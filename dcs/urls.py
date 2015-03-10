from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dcs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'dcs.views.home', name='home'), # mock, CHANGE later!
    url(r'^admin/', include(admin.site.urls)),
    url(r'^multimedia/', include('multimedia.urls')),
)

urlpatterns += staticfiles_urlpatterns()
