from django.contrib import admin
from .models import (
        Crew, Person, Role,
)


admin.site.register(Crew)
admin.site.register(Person)
admin.site.register(Role)
