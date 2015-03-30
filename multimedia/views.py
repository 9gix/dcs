from django.shortcuts import render
from .models import Book, Music


def book_list(request):
    books = Book.objects.all()
    return render(request, 'multimedia/book_list.html', {'multimedia': books, 'multimedia_type': 'Book'})


def book_detail(request, isbn13):
    book = Book.objects.get(isbn13=isbn13)
    return render(request, 'multimedia/book_detail.html', {'book': book})

def music_list(request):
    musics = Music.objects.all()
    return render(request, 'multimedia/music_list.html', {'multimedia': musics, 'multimedia_type': 'Music'})
