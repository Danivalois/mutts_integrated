import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
DEBUG = True  # ✅ Make sure this is set

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".vercel.app",
    os.getenv("VERCEL_URL", ""),  # Dynamically get Vercel's deployment URL
]

# ✅ Database Configuration (Using Supabase Transaction Pooler)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.mfusnfwxtnzzbmalklqw',  # Use Pooler User
        'PASSWORD': os.getenv('SUPABASE_DB_PASSWORD'),
        'HOST': 'aws-0-sa-east-1.pooler.supabase.com',  # Transaction Pooler
        'PORT': '6543',  # Transaction Pooler Port
        'OPTIONS': {
            'sslmode': 'require',  # Ensure SSL connection
        },
    }
}

# ✅ URLs & Templates
ROOT_URLCONF = 'mutts.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'mutts/templates'),  # Diretório global
            os.path.join(BASE_DIR, 'products/templates'),  # Diretório dos produtos
        ],
        'APP_DIRS': True,  # Deve estar True para buscar templates dentro dos apps
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




# ✅ Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # ✅ Your Apps
    'products',
    'customers',
    'orders',
]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ Static and Media Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # ✅ Add this to find static files
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ✅ CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    "https://mutts-django.vercel.app",
    "https://*.vercel.app"
]

# ✅ Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Timezone Settings
TIME_ZONE = "America/Sao_Paulo"
USE_TZ = True
