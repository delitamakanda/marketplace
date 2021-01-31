web: gunicorn marketplace.wsgi --workers 2 --log-file -
worker: celery -A marketplace worker beat -l info --without-gossip --without-mingle --without-heartbeat
release: python manage.py migrate
