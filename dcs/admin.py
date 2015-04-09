from django.contrib.admin import AdminSite
from django.conf.urls import patterns, include, url

from . import admin_urls

def list_book(request):
    return render(request, 'admin/book.html')


class DCSAdminSite(AdminSite):
    site_header = "Digital Content Store Basic Administration"
    site_title = "DCS Admin"

    def get_urls(self):
        urlpatterns = super().get_urls()
        urlpatterns += admin_urls.urlpatterns
        return urlpatterns

site = DCSAdminSite(name='dcsadmin')
