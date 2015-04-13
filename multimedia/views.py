from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import (
        Movie, Application, Book, Music, MultimediaImage, Multimedia
)
from crew.models import Crew
from review.models import MultimediaReview


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class MovieListView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    model = Movie


class MusicListView(ListView):
    model = Music


class MusicDetailView(DetailView):
    model = Music


class ApplicationListView(ListView):
    model = Application


class ApplicationDetailView(DetailView):
    model = Application


book_list = BookListView.as_view()
book_detail = BookDetailView.as_view()
movie_list = MovieListView.as_view()
movie_detail = MovieDetailView.as_view()
music_list = MusicListView.as_view()
music_detail = MusicDetailView.as_view()
application_list = ApplicationListView.as_view()
application_detail = ApplicationDetailView.as_view()


def search_result(request):
    keywords = request.GET.get('keyword')
    types = request.GET.getlist('types[]')
    category = request.GET.get('category')
    if (category == ''):
        category = None
    multimedia = Multimedia.objects.search(multimedia_types=types, keywords=keywords, category=category)

    for item in multimedia:
        item['url'] = '../' + str(item['url_prefix']) + '/' + str(item['url_suffix'])
        multimedia_image = MultimediaImage.objects.filter(multimedia_id=item['id']).first()
        if multimedia_image:
            item['thumbnail'] = multimedia_image.thumb150x150.url
        else:
            item['thumbnail'] = no_preview_150
    return render(request, 'multimedia/search_result.html', {'multimedia': multimedia, 'multimedia_type': 'Result'})

def advanced_search(request):
    return render(request, 'multimedia/advanced_search.html')
