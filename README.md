# CS2102: Digital Content Store

Digital Content Store Project (Semester 2, 2014/2015).

## Documentation

[ER Models][erd]

## Setup

```

# Install requirement
pip install -r requirements.txt

# Migrate Database
python dcs/manage.py migrate

# Create Super USer
python dcs/manage.py createsuperuser

# Start Local Server
python dcs/manage.py runserver
```

## Resources

* ER Modeling: [MySQL Workbench][mysql-workbench]
* Web Framework: [Django][django]

## Core Developer

* Diga
* Eugene
* John
* Michael
* Nathan

[mysql-workbench]: http://dev.mysql.com/downloads/workbench/
[django]: https://www.djangoproject.com/
[erd]: docs/erd.svg
