# Local settings for dcs project.  
LOCAL_SETTINGS = True
from dcs.settings import *

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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tik8g&=7)8mjbv@ji2r#=7i_yz0n_)_uu8%ad#0^vkks40%e5h'
