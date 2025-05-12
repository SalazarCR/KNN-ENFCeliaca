from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario_paciente, name='formulario_paciente'),
    path('historial/', views.historial_pacientes, name='historial_pacientes'),
]
