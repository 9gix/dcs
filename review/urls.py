from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<multimedia_id>\d+)/$', views.addReview,
        name='multimedia_review'),
]
