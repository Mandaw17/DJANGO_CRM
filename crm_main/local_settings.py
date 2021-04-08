import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_crm',
        'USER': 'root',
        'PASSWORD': 'passer',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'another': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd93ove0iknaav4',
        'USER': 'kixsocstmvohye',
        'PASSWORD': '6c9d339010b93f6873ae55f66c1ee812d1c00984130816a71df24e15dec7de4f',
        'HOST': 'ec2-107-22-245-82.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['another'].update(db_from_env)