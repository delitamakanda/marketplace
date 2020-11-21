# Marketplace

### How to init project

```bash
python3 -m venv env
source env/bin/activate

django-admin startproject marketplace .
django-admin startapp catalog

python3 manage.py runserver_plus --cert-file cert.crt

or 

python3 manage.py runserver
```

### Resources
* https://django-paypal.readthedocs.io/en/stable/
* https://github.com/spookylukey/django-paypal
* Django 3 by example by Antonio Melé
