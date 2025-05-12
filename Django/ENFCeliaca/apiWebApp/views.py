import pickle
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
from .forms import CeliacaForm

# Cargar el modelo entrenado KNN desde un archivo pickle
def load_knn_model():
    with open('apiWebApp/ml_models/knn_model.pkl', 'rb') as model_file:
        knn_model = pickle.load(model_file)
    return knn_model

# Cargar el dataset (si lo necesitas para alguna validación o para agregar nuevos datos)
def load_dataset():
    dataset = pd.read_csv('apiWebApp/ml_models/dataset.csv')
    return dataset

# Vista para procesar el formulario y realizar la predicción
def predict_celiaca(request):
    # Cargar el modelo y el dataset
    knn_model = load_knn_model()
    dataset = load_dataset()

    prediction = None
    probability = None

    if request.method == 'POST':
        # Recibir los datos del formulario
        form = CeliacaForm(request.POST)

        if form.is_valid():
            # Obtener los datos del formulario
            data = {
                'age': form.cleaned_data['age'],
                'gender': form.cleaned_data['gender'],
                'diabetes': form.cleaned_data['diabetes'],
                'diabetes_type': form.cleaned_data['diabetes_type'],
                'diarrhoea': form.cleaned_data['diarrhoea'],
                'short_stature': form.cleaned_data['short_stature'],
                'sticky_stool': form.cleaned_data['sticky_stool'],
                'weight_loss': form.cleaned_data['weight_loss'],
                'iga': form.cleaned_data['iga'],
                'igg': form.cleaned_data['igg'],
                'igm': form.cleaned_data['igm'],
            }

            # Convertir los datos del formulario en un DataFrame para hacer la predicción
            input_data = pd.DataFrame([data])

            # Realizar la predicción
            prediction = knn_model.predict(input_data)
            probability = knn_model.predict_proba(input_data)

            # Convertir las probabilidades a porcentaje
            probability = probability[0][1] * 100  # Usamos la probabilidad de la clase 1

    else:
        form = CeliacaForm()

    # Mostrar el resultado de la predicción y la probabilidad en la plantilla
    return render(request, 'form_template.html', {
        'form': form,
        'prediction': prediction,
        'probability': probability
    })
