from django.shortcuts import render, redirect
import pickle
import numpy as np



# Cargar modelo y codificadores
with open("modelo_knn.pkl", "rb") as f:
    modelo = pickle.load(f)

with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

# Cargar precisión
try:
    with open("precision_modelo.txt", "r") as f:
        precision = f.read().strip()
except FileNotFoundError:
    precision = "No disponible"

# Lista de síntomas esperados
sintomas_lista = [
    "Micción excesiva",
    "Sed excesiva",
    "Pérdida de peso repentina",
    "Debilidad",
    "Hambre excesiva",
    "Infección genital por hongos",
    "Visión borrosa",
    "Picazón",
    "Irritabilidad",
    "Cicatrización lenta",
    "Parálisis parcial",
    "Rigidez muscular",
    "Alopecia",
    "Obesidad"
]

# Valores válidos conocidos (ajustar según lo entrenado)
valores_genero_validos = label_encoders["Género"].classes_.tolist()
valores_sintoma_validos = ["Si", "No"]

def portada_view(request):
    return render(request, "portada.html")

def diagnostico_view(request):
    resultado = None
    prob_negativo = None
    prob_positivo = None
    alerta = ""

    valores = {
        "edad": "",
        "genero": "",
        "sintomas": {s: "" for s in sintomas_lista}
    }

    if request.method == "POST":
        if "limpiar" in request.POST:
            return redirect("diagnostico")

        edad = request.POST.get("edad", "")
        genero = request.POST.get("genero", "")
        sintomas = {s: request.POST.get(s, "") for s in sintomas_lista}

        valores["edad"] = edad
        valores["genero"] = genero
        valores["sintomas"] = sintomas

        if not edad or genero not in valores_genero_validos or any(val not in valores_sintoma_validos for val in sintomas.values()):
            alerta = "Por favor, complete todos los campos correctamente."
        else:
            try:
                edad = int(edad)
                genero_encoded = label_encoders["Género"].transform([genero])[0]
                sintomas_encoded = [
                    label_encoders[s].transform([val])[0] for s, val in sintomas.items()
                ]

                datos = [edad, genero_encoded] + sintomas_encoded
                entrada = np.array(datos).reshape(1, -1)

                prediccion = modelo.predict(entrada)[0]
                probabilidades = modelo.predict_proba(entrada)[0]

                resultado = "Positivo" if prediccion == 1 else "Negativo"
                prob_negativo = round(probabilidades[0] * 100, 2)
                prob_positivo = round(probabilidades[1] * 100, 2)

            except Exception as e:
                alerta = f"Error al procesar la solicitud: {str(e)}"

    return render(request, "formulario.html", {
        "resultado": resultado,
        "prob_negativo": prob_negativo,
        "prob_positivo": prob_positivo,
        "precision": precision,
        "sintomas_lista": sintomas_lista,
        "valores": valores,
        "alerta": alerta,
        "generos": valores_genero_validos
    })




