from django.contrib import admin
from .models import (
        Crew, Organization, Person, Role,
)


admin.site.register(Crew)
admin.site.register(Organization)
admin.site.register(Person)
admin.site.register(Role)
