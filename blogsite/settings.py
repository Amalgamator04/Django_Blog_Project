import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-replace-me-with-a-secure-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogsite.wsgi.application'

import urllib.parse as urlparse

# Support a single DATABASE_URL environment variable (e.g. mysql://user:pass@host:port/dbname)
db_url = os.environ.get('DATABASE_URL') or os.environ.get('RENDER_DATABASE_URL') or os.environ.get('CLEARDB_DATABASE_URL')

if db_url:
    parsed = urlparse.urlparse(db_url)
    db_scheme = parsed.scheme
    if db_scheme.startswith('mysql') or db_scheme == 'mysql':
        engine = 'django.db.backends.mysql'
    elif db_scheme.startswith('postgres') or db_scheme == 'postgres':
        engine = 'django.db.backends.postgresql'
    else:
        engine = 'django.db.backends.mysql'

    DATABASES = {
        'default': {
            'ENGINE': engine,
            'NAME': parsed.path.lstrip('/'),
            'USER': parsed.username or os.environ.get('DATABASE_USER', 'root'),
            'PASSWORD': parsed.password or os.environ.get('DATABASE_PASSWORD', ''),
            'HOST': parsed.hostname or os.environ.get('DATABASE_HOST', '127.0.0.1'),
            'PORT': parsed.port or os.environ.get('DATABASE_PORT', '3306'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DATABASE_NAME', 'blog_post'),
            'USER': os.environ.get('DATABASE_USER', 'root'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD', '7303025805pps'),
            'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
            'PORT': os.environ.get('DATABASE_PORT', '3306'),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise static files storage for efficient serving in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
