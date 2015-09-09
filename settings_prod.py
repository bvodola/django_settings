import os

"""
Main Settings
"""
DEBUG = False
ALLOWED_HOSTS = []
ADMINS = (('Name', 'email'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
Database
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': ''
    }
}

"""
Static files
"""
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

"""
E-mail settings
"""
EMAIL_HOST = 'smtp.YOURSERVER.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''
SERVER_EMAIL = ''