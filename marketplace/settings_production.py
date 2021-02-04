import os
from marketplace.settings import *
import dj_database_url

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*', ]

# email admin

SERVER_EMAIL = config('ADMIN_EMAIL')

ADMINS = [
  (config('ADMIN_NAME'), config('ADMIN_EMAIL')),
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('SENDGRID_SERVER')
EMAIL_PORT = config('SENDGRID_PORT')
EMAIL_HOST_USER = config('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = config('SENDGRID_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_TIMEOUT = 500

CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
