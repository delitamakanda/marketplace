import os

from marketplace.settings import *

if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': os.getenv('GOOGLE_APP_ENGINE_HOST'),
            'NAME': os.getenv('GOOGLE_APP_ENGINE_NAME'),
            'USER': os.getenv('GOOGLE_APP_ENGINE_USER'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('GOOGLE_APP_ENGINE_NAME'),
            'USER': os.getenv('GOOGLE_APP_ENGINE_USER'),
            'PASSWORD': os.getenv('GOOGLE_APP_ENGINE_PASSWORD'),
            'HOST': os.getenv('GOOGLE_APP_ENGINE_HOST'),
            'PORT': os.getenv('GOOGLE_APP_ENGINE_PORT'),
        }
    }
