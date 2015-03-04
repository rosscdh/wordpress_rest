# wordpress_rest

Basic REST api around wordpress database

NOTE
====

This is still in pre-alpha stages. It does not enforce the WP rules and things (for the sake of speed and accessability).

But it is a fully fledged rest api and I'll be working to make things like creating categories and tags etc simpler. And then creating terms even more simpler (a few tables get updated at the same time).


Installation
============

1. git clone https://github.com/rosscdh/wordpress_rest.git
2. edit settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wordpress_dev',              # Enter database name
        'HOST': '127.0.0.1',                  # Enter host
        'USER': '',                           # Enter username
        'PASSWORD': '',                       # Password
    }
}
```

3. pip install -r requirements.txt
4. ./manage.py runserver_plus --threaded 127.0.0.1:8000
