import dotenv
from os import getenv
dotenv.load_dotenv(dotenv.find_dotenv())
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': getenv("OPEN_PORT"),
        'NAME': getenv("NAME_DB"),
        'USER': getenv("USER"),
        'PASSWORD': getenv("PASS"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = getenv("SECRET_KEY")

TIME_ZONE = getenv("TIME_ZONE")

USE_TZ = True
