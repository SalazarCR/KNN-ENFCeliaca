# CeliacaWebApp/urls.py

from django.contrib import admin
from django.urls import path, include  # include para importar las URLs de apiWebApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', include('apiWebApp.urls')),  # Ruta que carga las URLs de apiWebApp
]
