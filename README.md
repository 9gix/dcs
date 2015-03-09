# CS2102: Digital Content Store

Digital Content Store Project (Semester 2, 2014/2015).

## Documentation

[ER Models][erd]

## Setup

Python 3

```
# Clone Project
git clone git@github.com:exclusive-gix/cs2102-store.git dcs
cd dcs

# Install requirement
pip install -r requirements.txt

# Configure Project
cp dcs/__local_settings.py dcs/local_settings.py

# Migrate Database
python manage.py migrate

# Create Super User
python manage.py createsuperuser

# Start Local Server
python manage.py runserver
```

## Resources

* ER Modeling: [MySQL Workbench][mysql-workbench]
* Web Framework (Server): [Django][django]
* Web Framework (Client): [Backbone.js][backbonejs]

## Core Developer

* Diga
* Eugene
* John
* Michael
* Nathan

[mysql-workbench]: http://dev.mysql.com/downloads/workbench/
[django]: https://www.djangoproject.com/
[backbonejs]: http://backbonejs.org/
[erd]: docs/erd.svg
