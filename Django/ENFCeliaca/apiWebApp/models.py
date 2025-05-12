from django.db import models

class PatientData(models.Model):
    AGE = models.IntegerField()
    GENDER = models.IntegerField(choices=[(0, 'Masculino'), (1, 'Femenino')])
    DIABETES = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')])
    DIABETES_TYPE = models.IntegerField(choices=[(1, 'Tipo 1'), (2, 'Tipo 2')])
    DIARRHOEA = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')])
    SHORT_STATURE = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')])
    STICKY_STOOL = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')])
    WEIGHT_LOSS = models.IntegerField(choices=[(0, 'No'), (1, 'Sí')])
    IGA = models.FloatField()
    IGG = models.FloatField()
    IGM = models.FloatField()

    # Campos de predicción
    DISEASE_DIAGOSE = models.IntegerField(choices=[(0, 'Negativo'), (1, 'Positivo')])
    PROBABILITY = models.FloatField(help_text="Probabilidad de predicción en %")

    def __str__(self):
        return f"Paciente {self.id} - Diagnóstico: {'Sí' if self.DISEASE_DIAGOSE else 'No'}"
