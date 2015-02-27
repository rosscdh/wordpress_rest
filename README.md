# wordpress_rest

Basic REST api around wordpress database


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