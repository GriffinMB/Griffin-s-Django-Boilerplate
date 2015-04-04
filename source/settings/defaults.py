"""
Django settings for griffins_django_boilerplate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    ("griffin"),
)
ALLOWED_HOSTS = (
    'django.org',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TEMPLATE_DEBUG = False

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Application definition

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = None

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    #django-compressor
    'compressor.finders.CompressorFinder',
)

ROOT_URLCONF = 'settings.urls'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
def get_path(*args):
    return os.path.realpath(os.path.join(*args))

BASE_DIR = get_path(os.path.dirname(__file__), "../")
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = get_path(BASE_DIR, "../", '.tmp', 'static')
STATICFILES_DIRS = (get_path(BASE_DIR, '../public'),)
TEMPLATE_DIRS = (get_path(BASE_DIR, 'templates'),)

ADMIN_NAMESPACEE = 'admin'

INSTALLED_APPS = (
    # DJANGO APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # THIRD PATY APPS
    'compressor',

    # LOCAL APPS
)

COMPRESS_ENABLED = True
COMPASS_COMMAND = ' && '.join([
    'cd %s' % get_path(BASE_DIR, '../', 'public'),
    'sass --scss --compass {infile} {outfile}',
])

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', COMPASS_COMMAND),
)

# WSGI_APPLICATION = 'griffins_django_boilerplate.wsgi.application'
