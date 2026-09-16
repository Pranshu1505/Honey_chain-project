from .base import *
import dj_database_url
from decouple import config

DEBUG = False
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='.onrender.com').split(',')

# Whitenoise for static files
MIDDLEWARE = list(MIDDLEWARE)
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Database (Render Postgres)
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# CORS - Vercel frontend URL yahan daalo (deploy hone ke baad update karna)
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='https://your-app-name.vercel.app').split(',')

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
