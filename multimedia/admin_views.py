from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic.edit import (
        FormMixin, ProcessFormView, DeletionMixin
)

from . import forms
from .models import Book

class ListBookView(View):
    template_name = 'multimedia/admin/index.html'

    def get(self, request, *args, **kwargs):
        context = {'items': []}
        context['items'] = Book.objects.all()
        for item in context['items']:
            item['admin_url'] = reverse('dcsadmin:book:edit',
                    kwargs={'pk': item['id'],})
        return render(request, self.template_name, context)


class AddBookView(FormMixin, ProcessFormView, View):

    template_name = 'multimedia/admin/add.html'
    form_class = forms.BookAdminForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.insert()
            return redirect('dcsadmin:book:index')
        context = {'form': form}
        return render(request, self.template_name, context)

class EditBookView(FormMixin, ProcessFormView, View):

    template_name = 'multimedia/admin/edit.html'
    form_class = forms.BookAdminForm

    def get(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs['pk'])
        form = self.form_class(book)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('dcsadmin:book:index')
        context = {'form': form}
        return render(request, self.template_name, context)

class DeleteBookView(View):
    def post(self, request, *args, **kwargs):
        Book.objects.delete(id=kwargs.get('pk'))
        return redirect('dcsadmin:book:index')

    

