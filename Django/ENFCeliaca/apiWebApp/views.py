from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CeliacaPredictionSerializer
import pickle
import numpy as np
from django.conf import settings

# Cargar el modelo KNN previamente entrenado
with open('MLENFCeliaca/modelo_knn.pkl', 'rb') as f:
    modelo_knn = pickle.load(f)

class CeliacaPredictionView(APIView):
    def post(self, request):
        # Usamos el serializer para validar los datos del formulario
        serializer = CeliacaPredictionSerializer(data=request.data)
        if serializer.is_valid():
            # Obtener los datos para la predicción
            data = np.array([[  # Toma los valores del formulario y crea el array
                serializer.validated_data['AGE'],
                serializer.validated_data['GENDER'],
                serializer.validated_data['DIABETES'],
                serializer.validated_data['DIARRHOEA'],
                serializer.validated_data['SHORT_STATURE'],
                serializer.validated_data['STICKY_STOOL'],
                serializer.validated_data['WEIGHT_LOSS'],
                serializer.validated_data['IGA'],
                serializer.validated_data['IGG'],
                serializer.validated_data['IGM'],
                serializer.validated_data['DISEASE_DIAGNOSE']
            ]])
            
            # Realizar la predicción
            prediction = knn_mm.predict(data)
            probability = knn_mm.predict_proba(data)
            
            # Devolver la respuesta
            response = {
                'prediction': 'Enfermo' if prediction[0] == 1 else 'No enfermo',
                'probability': probability[0][1] * 100  # Probabilidad de estar enfermo
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)