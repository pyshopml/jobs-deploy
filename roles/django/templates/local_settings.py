# coding: utf-8
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ postgresql_database }}',
        'USER': '{{ postgresql_user }}',
        'PASSWORD': '{{ postgresql_user_password }}',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_unicode_ci',
        }
    }
}

DEBUG = {{ debug }}
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = os.path.abspath(os.path.join("{{ project_dir }}", "static"))
MEDIA_ROOT = os.path.abspath(os.path.join("{{ project_dir }}", "media"))
