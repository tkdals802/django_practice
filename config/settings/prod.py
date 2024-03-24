from .base import *

ALLOWED_HOSTS = ['3.37.246.178']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '7EEmw}49E`H.l-Y+hk,STi%$TVP-aGx{',
        'HOST': 'ls-f5c0be1747adc337bae3e247ec6a6215aa3e3acb.cjscg6yum5gt.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}