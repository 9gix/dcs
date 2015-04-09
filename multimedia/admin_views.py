from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import (
        FormMixin, ProcessFormView, DeletionMixin
)

from . import forms

class ListBookView(View):
    template_name = 'multimedia/admin/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class DetailBookView(View):
    template_name = 'multimedia/admin/detail.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class AddBookView(FormMixin, ProcessFormView, View):

    template_name = 'multimedia/admin/add.html'
    form_class = forms.BookAdminForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, reqeust, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('admin:book:index')
        context = {'form': form}
        return render(request, self.template_name, context)

class EditBookView(FormMixin, ProcessFormView, View):

    template_name = 'multimedia/admin/edit.html'
    form_class = forms.BookAdminForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, reqeust, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('admin:book:index')
        context = {'form': form}
        return render(request, self.template_name, context)

class DeleteBookView(DeletionMixin, View):
    pass

