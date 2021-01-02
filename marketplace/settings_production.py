import os
from marketplace.settings import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*',]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

