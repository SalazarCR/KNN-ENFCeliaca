from django.contrib import admin
from django.urls import path
from apiWebApp.views import home, predict_view  # Importa las vistas

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('predict/', predict_view),  # Ruta para la vista de predicción
    path('', home),  # Ruta para la página de inicio
]
