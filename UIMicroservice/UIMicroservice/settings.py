import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Get service URLs from environment variables
TASK_SERVICE_URL = os.getenv('TASK_SERVICE_URL')
USER_SERVICE_URL = os.getenv('USER_SERVICE_URL')

SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
DEBUG = os.getenv('DEBUG', 'True') == 'True'


ALLOWED_HOSTS = ['localhost', '127.0.0.1']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'UIMicroservice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend/templates'],
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

WSGI_APPLICATION = 'UIMicroservice.wsgi.application'

# Minimal database configuration for Django to run
# settings.py





STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "frontend/static"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
