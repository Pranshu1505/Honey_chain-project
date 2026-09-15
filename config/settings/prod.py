# from .base import *
# import dj_database_url
# from decouple import config

# DEBUG = False
# SECRET_KEY = config('SECRET_KEY')
# ALLOWED_HOSTS = ['.onrender.com']

# # Whitenoise for static files
# MIDDLEWARE = list(MIDDLEWARE)
# MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # Database (Render Postgres)
# DATABASES = {
#     'default': dj_database_url.config(default=config('DATABASE_URL'))
# }

# # CORS - Netlify frontend URL yahan daalo (deploy hone ke baad update karna)
# CORS_ALLOWED_ORIGINS = [
#     "https://your-app-name.netlify.app",
# ]