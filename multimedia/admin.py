from django.contrib import admin
from .models import (
        Organisation, Multimedia, Book, Movie, Application,
        Album, Music, AlbumMusic,
        Category, MultimediaCategory,
        MultimediaContent, MultimediaImage
)
from dcs import admin as dcs_admin

class MultimediaImageInline(admin.TabularInline):
    model = MultimediaImage
    extra = 1

class MultimediaAdmin(admin.ModelAdmin):
    inlines = [
        MultimediaImageInline,
    ]


admin.site.register(Organisation)
admin.site.register(Book, MultimediaAdmin)
admin.site.register(Movie, MultimediaAdmin)
admin.site.register(Application, MultimediaAdmin)
admin.site.register(Music, MultimediaAdmin)
admin.site.register(Album)
admin.site.register(AlbumMusic)
admin.site.register(Category)
admin.site.register(MultimediaCategory)
admin.site.register(MultimediaContent)
admin.site.register(MultimediaImage)

#dcs_admin.site.register(Book)
