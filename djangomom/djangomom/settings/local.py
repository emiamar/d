from base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PROJECTS_DIRECTORY = os.path.join(BASE_DIR, '../', '../', '../')

STATICFILES_DIRS = [
    (os.path.join(BASE_DIR, '../', 'static')),
]

MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INSTALLED_APPS += ['debug_toolbar']
