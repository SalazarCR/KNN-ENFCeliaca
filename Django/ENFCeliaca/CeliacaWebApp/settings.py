from pathlib import Path
import os
from datetime import timedelta

# Base de directorios
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta (cámbiala por algo más seguro en producción)
SECRET_KEY = 'django-insecure-gdu-ehw5pdn%ue^s96=sixi1km9utm(g@nk!*dcc8m!=cj_)%_'

# Seguridad
DEBUG = True
ALLOWED_HOSTS = ['*']  # Cambiar esto por tus dominios en producción

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apiWebApp',  # Tu aplicación de la API
]

# Middleware
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

# Configuración de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'apiWebApp/templates'],  # Aquí se agrega la ruta de los templates
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
        'ENGINE': 'django.db.backends.sqlite3',  # Usa PostgreSQL o MySQL para producción
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
STATIC_URL = 'static/'  # URL para acceder a los archivos estáticos

# Aquí configuras la carpeta donde están tus archivos estáticos (por ejemplo, para tu desarrollo)
STATICFILES_DIRS = [BASE_DIR / 'static']


# El lugar donde se recopilarán los archivos estáticos para producción (usualmente en un directorio separado)
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Para producción

# Archivos multimedia (subidas)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Campo auto por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Tu frontend local
    "http://127.0.0.1:3000",  # Tu frontend local
]

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

# Configuración del correo (cambia a producción más tarde)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Para pruebas en desarrollo

# Seguridad en producción
# Cuando implementes en producción, habilita las siguientes configuraciones de seguridad
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 31536000  # 1 año
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True

# Expiración de sesiones y cookies
SESSION_COOKIE_AGE = timedelta(days=7).total_seconds()  # Duración de la sesión
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Cierra la sesión cuando el usuario cierre el navegador

# Configuración de logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',  # Cambiado de 'DEBUG' a 'INFO' para reducir el volumen de logs
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',  # Cambiado de 'DEBUG' a 'INFO' para reducir el volumen de logs
            'propagate': True,
        },
    },
}

# (Opcional) Configuración de caché (en producción puede ser necesario)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # Cambiar a un backend adecuado en producción
    }
}
