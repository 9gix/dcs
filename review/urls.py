from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<multimedia_id>\d+)/$', 'review.views.review', name='multimedia_review'),
]
