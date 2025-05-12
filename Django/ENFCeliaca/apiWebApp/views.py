from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd

# Esta es una vista simple que puedes personalizar según lo que necesites
def predict_view(request):
    # Aquí podrías agregar tu modelo de predicción y cualquier otra lógica.
    
    # Suponiendo que tienes alguna predicción, por ejemplo:
    # Crear algunos datos ficticios para ilustrar
    data = {
        'AGE': [30],
        'GENDER': [1],  # 1 para femenino
        'DIABETES': [1],  # 1 para sí
        'DIABETES_TYPE': [2],  # 2 para tipo 2
        'DIARRHOEA': [0],  # 0 para no
        'SHORT_STATURE': [0],  # 0 para no
        'STICKY_STOOL': [1],  # 1 para sí
        'WEIGHT_LOSS': [1],  # 1 para sí
        'IGA': [2.5],
        'IGG': [3.0],
        'IGM': [1.2],
    }
    
    # Convertir los datos a un DataFrame para mostrar (esto es solo un ejemplo)
    df = pd.DataFrame(data)
    
    # Aquí deberías colocar tu lógica de predicción, utilizando los datos en df.
    # Simulando una predicción:
    prediction = "Positivo"  # Este valor se puede obtener de tu modelo de predicción
    
    # Mostrar el resultado de la predicción
    response = f"Predicción de enfermedad: {prediction}. Datos utilizados: {df.to_html()}"
    
    return HttpResponse(response)
def home(request):
    return HttpResponse("<h1>Bienvenido a la página principal de predicción</h1>")
