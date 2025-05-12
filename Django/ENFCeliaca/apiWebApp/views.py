import numpy as np
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionInputSerializer
import os
from django.conf import settings

# Cargar el modelo entrenado
model_path = os.path.join(settings.BASE_DIR, 'MLENFCeliaca', 'modelo_knn.pkl')
with open(model_path, 'rb') as model_file:
    knn_model = pickle.load(model_file)

@api_view(['POST'])
def predict_disease(request):
    serializer = PredictionInputSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = serializer.validated_data
    features = np.array([[data[field] for field in serializer.fields]])

    prediction = knn_model.predict(features)
    probability = knn_model.predict_proba(features)[0]

    result = {
        'prediction': 'Enfermo' if prediction[0] == 1 else 'No Enfermo',
        'probability': {
            'No_tiene': round(probability[0], 4),
            'Si_tiene': round(probability[1], 4)
        }
    }
    return Response(result)
