from __future__ import absolute_import, unicode_literals


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'traugott',
        'USER': 'traugott',
        'PASSWORD': 'pa$$word',
        'HOST': 'localhost',
        'PORT': '',
    }
}