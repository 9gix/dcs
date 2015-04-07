# CS2102: Digital Content Store

Digital Content Store Project (Semester 2, 2014/2015).

## Documentation

[ER Models][erd]

## Setup

* Python 3
* MySQL Server

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

## Media folder
1. Download public media folder [here][media]
2. Unzip file on the project-level directory

## Database Guide

1. Create a Schema in MySQL
2. Configure database in `local_settings.py`

```
# Creating an empty migration:
python manage.py makemigrations --empty <app_name> <revision:optional>

# Executing migration script:
python manage.py migrate <app_name:optional> <revision:optional>

# Rollback application database migration:
python manage.py migrate <app_name> zero

# Database Reset (WARNING!! IRREVERSIBLE Destroy database)
python manage.py reset_db
```

# Migration Script Guide

```
# file: <app_name>/migrations/<rev>_<label>.py
# Execute SQL use RunSQL:
# https://docs.djangoproject.com/en/1.7/ref/migration-operations/#runsql

# Note: every forward migration must have its backward migration
# For example: a sql script for create table, 
# must have its corresponding drop table

# Create table sql script should be located in `schema` folder.
# These sql scripts will be loaded by django migration script.
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
[media]: https://dl.dropboxusercontent.com/u/10757226/public.zip
