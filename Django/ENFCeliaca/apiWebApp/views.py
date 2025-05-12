import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Cargar el modelo KNN
model_path = 'MLENFCeliaca/modelo_knn.pkl'
with open(model_path, 'rb') as f:
    knn_model = pickle.load(f)

# Etiquetas para las clases
clasificadores = ['No_tiene', 'Si_tiene']

@api_view(['POST'])
def predict_disease(request):
    try:
        # Obtener los datos enviados en formato JSON
        data = request.data
        features = np.array([
            data['AGE'],
            data['GENDER'],
            data['DIABETES'],
            data['DIABETES_TYPE'],
            data['DIARRHOEA'],
            data['SHORT_STATURE'],
            data['STICKY_STOOL'],
            data['WEIGHT_LOSS'],
            data['IGA'],
            data['IGG'],
            data['IGM']
        ]).reshape(1, -1)

        # Realizar la predicción
        prediction = knn_model.predict(features)
        prediction_prob = knn_model.predict_proba(features)

        # Resultado
        result = {
            'prediction': clasificadores[int(prediction[0])],
            'probability': {
                'No_tiene': prediction_prob[0][0],
                'Si_tiene': prediction_prob[0][1]
            }
        }

        return JsonResponse(result, status=status.HTTP_200_OK
