from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import MultimediaReview

def addReview(request, multimedia_id):
    comment = request.POST['comment']
    rating = request.POST['rating']
    newReview = MultimediaReview(
        user=request.user, multimedia_id=multimedia_id, comment=comment, rating=rating)
    newReview.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
