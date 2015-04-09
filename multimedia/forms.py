from django import forms
from .models import Book


class BookAdminForm(forms.ModelForm):
    model = Book


