"""
Django settings for djangomom project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import ConfigParser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE = os.path.normpath(
    os.path.join(BASE_DIR, '../', "../", "config.cfg")
)

config = ConfigParser.ConfigParser()
config.read(CONFIG_FILE)

admin = config.get('local', 'default_from_email')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ob$2^_qvzlbi2&z5bdb64@%s#wd5+-^2zu&iw%cvxy8(#&5e8g'

ALLOWED_HOSTS = []

ADMINS = [admin,]

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


LOCAL_APPS = [
    'modeller',
    'base',
    'project',
    'app',
    'endpoint',
    'rest_framework',
    'core',
    'account',
    'django_tables2',
    'crispy_forms',
    'webfaction',
    'serializer',
    'mail',
    'django_extlog',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_extlog.middleware.AuditLoggingMiddleware',
]

ROOT_URLCONF = 'djangomom.urls'

CRISPY_TEMPLATE_PACK = "bootstrap3"

LOGIN_URL = '/signin/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.normpath(os.path.join(BASE_DIR, '../', 'templates'))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangomom.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.normpath(os.path.join(BASE_DIR, '../', 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'basic',
            'filename': os.path.join(BASE_DIR, 'logs/py_local.log'),
        },
    },
    'loggers': {
        'base': {
            'handlers': ['default', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,

        },
        'project': {
            'handlers': ['default', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'modeller': {
            'handlers': ['default', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'app': {
            'handlers': ['default', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'account': {
            'handlers': ['default', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'mail': {
            'handlers': ['default', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


GENERIC_TABLE_ATTRS = {
    'class': 'table table-striped dataTable no-footer',
    'id': 'dataTables-example1',
    'role': "grid",
    'aria-describedby': "dataTables-example_info"
}


EMAIL_USE_TLS = True
EMAIL_HOST = config.get('local', 'email_host')
EMAIL_HOST_USER = config.get('local', 'email_host_user')
DEFAULT_FROM_EMAIL = admin
SERVER_EMAIL = admin
EMAIL_HOST_PASSWORD = config.get('local', 'email_host_password')
