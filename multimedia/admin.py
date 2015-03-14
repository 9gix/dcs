from django.contrib import admin
from .models import (
        Multimedia, Book,
        Album, Music, AlbumMusic,
        Category, MultimediaCategory,
        MultimediaContent, MultimediaReview
)


admin.site.register(Book)
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(AlbumMusic)
admin.site.register(Category)
admin.site.register(MultimediaCategory)
admin.site.register(MultimediaContent)
admin.site.register(MultimediaReview)
