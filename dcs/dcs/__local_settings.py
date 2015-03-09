# Local settings for dcs project.  
LOCAL_SETTINGS = True
from settings import *

DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dcs',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''
