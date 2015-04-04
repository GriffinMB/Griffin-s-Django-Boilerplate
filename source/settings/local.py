import sys

from .defaults import *

DEBUG = LOCAL_SERVE = TEMPLATE_DEBUG = True

SECRET_KEY = 'abcd123!'

DATABASES = {
		'default': {
				'ENGINE': 'django.db.backends.postgresql_psycopg2',
				'NAME': 'blog',
				'USER': 'Michael',
				'PASSWORD': '',
				'HOST': '',
				'PORT': '',
		}
}
