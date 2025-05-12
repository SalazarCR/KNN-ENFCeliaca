from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apiWebApp.urls')),  # Aquí incluimos las rutas de la API
]
