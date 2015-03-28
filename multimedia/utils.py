
def dictfetchall(cursor):
    """
    Fetch data from django.db.connection.cursor
    and return an iterator of dictionary.
    """
    desc = cursor.description
    for row in cursor.fetchall():
        yield dict(zip([col[0] for col in desc], row))

def dictfetchone(cursor):
    """
    Fetch data from django.db.connection.cursor
    and return a dictionary.
    """
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))
