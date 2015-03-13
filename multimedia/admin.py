from django.contrib import admin
from .models import (
        Multimedia, Application, Book,
        Album, Music, Movie, AlbumMusic
)


admin.site.register(Application)
admin.site.register(Book)
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(Movie)
admin.site.register(AlbumMusic)