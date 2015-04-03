from django.shortcuts import render
from .models import Book, MultimediaImage


def book_list(request):
    books = Book.objects.all()
    book_ids = list(map(lambda book: book['id'], books))
    #import ipdb; ipdb.set_trace()
    multimedia_images = MultimediaImage.objects.filter(multimedia_id__in=book_ids)
    for book in books:
        multimedia_image = multimedia_images.filter(multimedia_id=book['id']).first()
        if multimedia_image:
            book['thumbnail'] = multimedia_image.thumbnail.url
        else:
            book['thumbnail'] = ''
    return render(request, 'multimedia/book_list.html', {'multimedia': books, 'multimedia_type': 'Book'})


def book_detail(request, isbn13):
    book = Book.objects.get(isbn13=isbn13)
    return render(request, 'multimedia/book_detail.html', {'book': book})
