import os
from marketplace.settings import *
import dj_database_url
import django_heroku

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*', ]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(
    locals(),
    allowed_hosts=True,
    secret_key=True,
    staticfiles=False,
    test_runner=True,
    logging=True,
)
