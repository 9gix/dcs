from django.db import connection
from django.db import models
from django.core.urlresolvers import reverse

from multimedia.utils import (
    dictfetchall, dictfetchone
)

class CrewManager(models.Manager):
    def filter(self, *args, **kwargs):
        crews = []
        with connection.cursor() as c:
            c.execute('''
                SELECT crew.id, person.name AS person, role.name AS role
                FROM crew, role, person
                WHERE crew.person_id = person.id
                  AND crew.role_id = role.id
                  AND crew.multimedia_id = %s
                  AND role.name = %s;
            ''', [kwargs['multimedia_id'], kwargs['role'],])

            for crew in dictfetchall(c):
                crews.append(crew)

        return crews
