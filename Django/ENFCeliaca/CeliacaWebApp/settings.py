from pathlib import Path
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

# Asegúrate de que este directorio exista
STATICFILES_DIRS = [
    BASE_DIR / "static",  
]

SECRET_KEY = 'django-insecure-gdu-ehw5pdn%ue^s96=sixi1km9utm(g@nk!*dcc8m!=cj_)%_'

DEBUG = True

ALLOWED_HOSTS = ['*']  # Cambia esto por tus dominios en producción

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # Debe estar solo una vez
    'apiWebApp',  # Tu aplicación personalizada
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Asegúrate de que esté al principio
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CeliacaWebApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Carpeta para templates si usas vistas HTML
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CeliacaWebApp.wsgi.application'

# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Para producción, usa PostgreSQL o MySQL
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internacionalización
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JS, etc.)
STATIC_URL = 'static/'

# Reemplaza esto para asegurarte de que Django sirva tus archivos estáticos correctamente
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Para producción, donde se recopilan los archivos estáticos

# Archivos multimedia (subidas)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Campo auto por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de CORS (si tienes frontend separado)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Tu frontend local
    "http://127.0.0.1:3000",  # Tu frontend local
]

# Permitir cookies con credenciales
CORS_ALLOW_CREDENTIALS = True

# Configuración para REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

# Configuración para el correo (ajústalo según tus necesidades)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Cambiar a producción más tarde
# Si usas SMTP, configura las opciones siguientes:
# EMAIL_HOST = 'smtp.tu-servidor.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'tu-correo'
# EMAIL_HOST_PASSWORD = 'tu-password'

# Seguridad (para producción)
# Cuando implementes en producción, asegúrate de habilitar las configuraciones de seguridad
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 31536000  # 1 año
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True

# Configuración de expiración de sesiones y cookies
SESSION_COOKIE_AGE = timedelta(days=7).total_seconds()  # Define la duración de la sesión
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Cierra la sesión cuando el usuario cierre el navegador

# Configuración de logging (útil para producción)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# (Opcional) Configuración de caché (en producción puede ser necesario)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # Usa otro backend en producción
    }
}

# Define tu middleware y configuraciones adicionales para mejorar el rendimiento y la seguridad
