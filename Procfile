web: gunicorn marketplace.wsgi:application --preload --log-file -
worker: celery -A marketplace worker beat -l info --without-gossip --without-mingle --without-heartbeat
