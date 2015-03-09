from django.contrib import admin
from .models import (
        Multimedia, Application, Book,
        Album, Music, Movie,
        Crew, Organization, Person, Role,
)


admin.site.register(Application)
admin.site.register(Book)
admin.site.register(Album)
admin.site.register(Music)
admin.site.register(Movie)
admin.site.register(Crew)
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(Role)
