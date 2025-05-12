from django.urls import path
from .views import CeliacaPredictionView

urlpatterns = [
    path('predict/', CeliacaPredictionView.as_view(), name='predict'),
]
