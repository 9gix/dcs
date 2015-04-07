from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dcs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'dcs.views.home', name='home'), # mock, CHANGE later!
    url(r'^nimda/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^carts/', include('transaction.urls', namespace='carts')),
    url(r'^', include('multimedia.urls', namespace='multimedia')),
    
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
