from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import MultimediaReview

def review(request, multimedia_id):
    comment = request.POST['comment']
    rating = request.POST['rating']
    newReview = MultimediaReview(multimedia_id, comment, rating)
    newReview.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
