from django.contrib import admin
from .models import (
        Crew, Organisation, Person, Role,
)


admin.site.register(Crew)
admin.site.register(Organisation)
admin.site.register(Person)
admin.site.register(Role)
