"""
Django settings for kypershop_app project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p453vm3mcaz9#e*v9mr=#@o9kfd(mas@u9bc^btj@+3bkh&lx+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# Templates Directory
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")


#static files
STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#Location of static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')

#media files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',        
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_gis',
    'drf_yasg',
    'django.contrib.gis',
]

#local App´s
LOCAL_APPS = [
    'markets',
    'orders',
    'users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kypershop_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'kypershop_app.wsgi.application'


REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'kypershop_db',
        'USER': 'user_db',
        'PASSWORD': 'kypershop2020$$',
        'HOST': 'rds-instance-kypershop.cuur8bbcuhzo.us-east-1.rds.amazonaws.com',
        'PORT': '5432',

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

