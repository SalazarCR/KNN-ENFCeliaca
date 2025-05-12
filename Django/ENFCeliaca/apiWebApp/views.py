from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import os
import numpy as np
from django.conf import settings

class CeliacaPredictionView(APIView):
    def post(self, request):
        try:
            # Asegúrate de pasar los datos con keys correctas
            datos = request.data.get("datos")

            if datos is None:
                return Response({"error": "Faltan los datos."}, status=status.HTTP_400_BAD_REQUEST)

            # Cargar modelo
            modelo_path = os.path.join(settings.BASE_DIR, 'modelo', 'modelo_entrenado.pkl')
            modelo = joblib.load(modelo_path)

            # Convertir datos en array
            input_array = np.array(datos).reshape(1, -1)

            # Realizar predicción
            prediccion = modelo.predict(input_array)

            return Response({"prediccion": int(prediccion[0])})

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        return Response({"message": "Este endpoint solo acepta POST."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
