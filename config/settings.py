"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv() # Loads environment variables from the local .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# VITAL SECURITY FIXES
# Reads from environment variable set on Render, or from .env locally
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: Turn DEBUG OFF in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True' 

# --- ALLOWED HOSTS ---
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

# Add the render domain if it exists (Render sets this later)
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# If DEBUG is True (local environment), allow all hosts
if DEBUG:
    ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # VITAL: WhiteNoise must be here to handle static files in production
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'portfolio.context_processors.profile_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(
        # Reads from DATABASE_URL environment variable set by Render
        default=os.environ.get('DATABASE_URL'), 
        conn_max_age=600
    )
}

# Password validation (omitted for brevity)

AUTHENTICATION_BACKENDS = [
    'portfolio.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Internationalization (omitted for brevity)

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# VITAL: Define the directory where Django will collect all static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# VITAL: Use WhiteNoise storage to manage compression, caching, and serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- CLOUDINARY CONFIGURATION ---
CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')

# Tell Django to use Cloudinary for uploaded files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

JAZZMIN_SETTINGS = {
    "site_title": "Lumi-Tech Admin",
    "site_header": "Lumi-Tech Portfolio",
    "site_brand": "Lumi-Tech",
    "welcome_sign": "Welcome to your Portfolio Dashboard",
    "copyright": "Lumi-Tech Ltd",
    "search_model": "portfolio.Project",
}

# --- EMAIL SETTINGS (Crucial for receiving contact forms) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'lumitechconsultant@gmail.com'
# VITAL: Reads password from environment variable
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') 
DEFAULT_FROM_EMAIL = 'Lumi-Tech Portfolio <lumitechconsultant@gmail.com>'
RECIPIENT_ADDRESS = 'lumitechconsultant@gmail.com'