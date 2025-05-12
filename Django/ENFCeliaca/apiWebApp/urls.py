from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_celiaca, name='predict_celiaca'),  # Ruta para la vista de predicción
]