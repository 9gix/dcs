from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<multimedia_id>\d+)/$', 'review.views.addReview', name='multimedia_review'),
]
