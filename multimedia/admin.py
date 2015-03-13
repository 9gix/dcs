from django.contrib import admin
from .models import (
        Multimedia, Application, Book,
        Album, Music, Movie,
        Category, MultimediaCategory,
        MultimediaContent, MultimediaReview,
)


admin.site.register(Application)
admin.site.register(Book)
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(MultimediaCategory)
admin.site.register(MultimediaContent)
admin.site.register(MultimediaReview)
