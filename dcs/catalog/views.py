from django.shortcuts import render
from .models import Book


def book_list(request):
    books = Book.all()
    return render(request, 'catalog/list.html', {'data': books})
