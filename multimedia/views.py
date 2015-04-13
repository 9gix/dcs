from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from .models import (
        Movie, Application, Book, Music, MultimediaImage, Multimedia
)
from crew.models import Crew
from review.models import MultimediaReview

no_preview = static('images/no-preview.png')
no_preview_150 = static('images/no-preview-150.png')

def book_list(request):
    books = Book.objects.all()
    book_ids = list(map(lambda book: book['id'], books))
    multimedia_images = MultimediaImage.objects.filter(multimedia_id__in=book_ids)

    for book in books:
        multimedia_image = multimedia_images.filter(multimedia_id=book['id']).first()
        if multimedia_image:
            book['thumbnail'] = multimedia_image.thumb150x150.url
        else:
            book['thumbnail'] = no_preview_150

        authors = Crew.objects.filterRole(multimedia_id=book['id'], role='Author')
        book['authors'] = authors

    return render(request, 'multimedia/book_list.html', {'multimedia': books, 'multimedia_type': 'Book'})


def book_detail(request, isbn13):
    book = Book.objects.get(isbn13=isbn13)

    authors = Crew.objects.filterRole(multimedia_id=book['id'], role='Author')
    book['authors'] = authors

    multimedia_images = MultimediaImage.objects.filter(multimedia_id=book['id'])
    image = multimedia_images.first()
    book['thumbnail'] = image.thumb250x250.url if image else no_preview

    reviews = MultimediaReview.objects.filter(multimedia_id=book['id'])

    return render(request, 'multimedia/book_detail.html',
        {'book': book, 'multimedia_id':book['id'], 'reviews':reviews})

def movie_list(request):
    movies = Movie.objects.all()

    for movie in movies:
        actors = Crew.objects.filterRole(multimedia_id=movie['id'], role = 'Actor')
        directors = Crew.objects.filterRole(multimedia_id=movie['id'], role = 'Director')
        movie['actors'] = actors
        movie['directors'] = directors

        minute = movie['duration'] // 60
        movie['duration_min'] = minute

        multimedia_image = MultimediaImage.objects.filter(multimedia_id=movie['id']).first()
        if multimedia_image:
            movie['thumbnail'] = multimedia_image.thumb150x150.url
        else:
            movie['thumbnail'] = no_preview_150

    return render(request, 'multimedia/movie_list.html', {'multimedia': movies, 'multimedia_type': 'Movie'})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    actors = Crew.objects.filterRole(multimedia_id=movie['id'], role = 'Actor')
    directors = Crew.objects.filterRole(multimedia_id=movie['id'], role = 'Director')
    movie['actors'] = actors
    movie['directors'] = directors

    minute = movie['duration'] // 60
    movie['duration_min'] = minute

    multimedia_images = MultimediaImage.objects.filter(multimedia_id=movie['id'])
    image = multimedia_images.first()
    movie['thumbnail'] = image.thumb250x250.url if image else no_preview_150

    reviews = MultimediaReview.objects.filter(multimedia_id=movie_id)

    return render(request, 'multimedia/movie_detail.html',
        {'movie': movie, 'multimedia_id': movie_id, 'reviews': reviews})

def music_list(request):
    musics = Music.objects.all()

    for music in musics:
        crews = Crew.objects.filter(multimedia_id=music['id'])
        music['crews'] = crews

        multimedia_image = MultimediaImage.objects.filter(multimedia_id=music['id']).first()
        if multimedia_image:
            music['thumbnail'] = multimedia_image.thumb150x150.url
        else:
            music['thumbnail'] = no_preview_150

    return render(request, 'multimedia/music_list.html', {'multimedia': musics, 'multimedia_type': 'Music'})

def music_detail(request, music_id):
    music = Music.objects.get(id=music_id)

    minute, second = divmod(music['duration'], 60)
    music['duration_min'] = minute
    music['duration_sec'] = second

    crews = Crew.objects.filter(multimedia_id=music_id)
    music['crews'] = crews

    multimedia_images = MultimediaImage.objects.filter(multimedia_id=music['id'])
    image = multimedia_images.first()
    music['thumbnail'] = image.thumb250x250.url if image else no_preview

    reviews = MultimediaReview.objects.filter(multimedia_id=music_id)

    return render(request, 'multimedia/music_detail.html',
        {'music': music, 'multimedia_id': music_id, 'reviews': reviews})

def application_list(request):
    applications = Application.objects.all()

    for application in applications:

        multimedia_image = MultimediaImage.objects.filter(multimedia_id=application['id']).first()
        if multimedia_image:
            application['thumbnail'] = multimedia_image.thumb150x150.url
        else: application['thumbnail'] = no_preview_150 
    return render(request, 'multimedia/application_list.html', {'multimedia': applications, 'multimedia_type': 'Application'})


def application_detail(request, application_id):
    application = Application.objects.get(id=application_id)

    multimedia_images = MultimediaImage.objects.filter(multimedia_id=application['id'])
    image = multimedia_images.first()
    application['thumbnail'] = image.thumb250x250.url if image else no_preview

    reviews = MultimediaReview.objects.filter(multimedia_id=application_id)

    return render(request, 'multimedia/application_detail.html',
        {'application': application, 'multimedia_id': application_id, 'reviews': reviews}) 

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
