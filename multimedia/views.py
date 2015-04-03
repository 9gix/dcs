from django.shortcuts import render
from .models import Book, Music
from crew.models import Crew


def book_list(request):
    books = Book.objects.all()
    return render(request, 'multimedia/book_list.html', {'multimedia': books, 'multimedia_type': 'Book'})


def book_detail(request, isbn13):
    book = Book.objects.get(isbn13=isbn13)
    return render(request, 'multimedia/book_detail.html', {'book': book})

def music_list(request):
    musics = Music.objects.all()

    for music in musics:
        crews = Crew.objects.filter(multimedia_id=music['id'])
        music['crews'] = crews

    return render(request, 'multimedia/music_list.html', {'multimedia': musics, 'multimedia_type': 'Music'})

def music_detail(request, music_id):
    music = Music.objects.get(id=music_id)
    crews = Crew.objects.filter(multimedia_id=music_id)
    music['crews'] = crews
    return render(request, 'multimedia/music_detail.html', {'music': music})
