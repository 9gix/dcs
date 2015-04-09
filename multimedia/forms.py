from django import forms
from .models import Book


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn13', 'isbn10', 'name', 'description', 'organisation']


