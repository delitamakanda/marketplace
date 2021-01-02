# Marketplace
![Django CI](https://github.com/delitamakanda/marketplace/workflows/Django%20CI/badge.svg?branch=main)
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


### Misc
1. https://www.mattlayman.com/blog/2020/hugo-blog-in-django-app/
2. https://opensource.com/article/20/11/django-rest-framework-serializers


### Make Hugo Pretty
1. https://themes.gohugo.io/hugo-ink/
2. https://themes.gohugo.io/tale-hugo/
3. https://themes.gohugo.io/theme/smol/
4. https://themes.gohugo.io/almeida-cv/
5. https://themes.gohugo.io/theme/simple-resume/


### Start Hugo
```bash
hugo server -D

# new post
hugo new posts/my-first-post.md
```

