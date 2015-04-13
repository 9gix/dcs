from django import forms
from .models import Book


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'price', 'categories', 'organisation',
                'isbn13', 'isbn10', 'published_on']

