"""
Django settings for studybuddy project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os, sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%izzhrjd!vk*mwofn4vx7(5fm*f=k2%i_3pkch3i1yfp2st9wv'#os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'studysite.apps.StudysiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'bootstrap5',
    'whitenoise.runserver_nostatic',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'studybuddy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'studysite' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'studybuddy.wsgi.application'


#if 'test' in sys.argv:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3eanse0roeke7',
        'USER': 'fjvnlxfiyrfyav',
        'PASSWORD': '8cc2f52d8381930ecd01e0319589a5236b844d49b3a7715ec36045eb41f10414',
        'HOST': 'ec2-52-86-177-34.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
# else:
#     DATABASES = {
#         'default':{
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': 'mydatabase'
#         }
#     }
    
    # db_from_env = dj_database_url.config(conn_max_age=600)
    # DATABASES['default'].update(db_from_env)
    

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Needed for Google Login

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

#instructions from https://www.youtube.com/watch?v=inQyZ7zFMHM

AWS_ACCESS_KEY_ID = 'AKIA4BMRTQ4IOAT5R4RQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'meganprofilebucket'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

SITE_ID = 4
#
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
SOCIALACCOUNT_LOGIN_ON_GET = True



LOGIN_REDIRECT_URL = '/studysite'
LOGOUT_REDIRECT_URL = '/studysite'

# Activate Django-Heroku.
# Use this code to avoid the psycopg2 / django-heroku error!  
# Do NOT import django-heroku above!
try:
    if 'HEROKU' in os.environ:
        import django_heroku
        django_heroku.settings(locals())
except ImportError:
    found = False

try:
    from studybuddy.local_settings import *
    print('imported local settings')
    print(STATIC_URL)
except ImportError:
    print('fail no local')
    pass
