from django.contrib import admin
from .models import PatientData

@admin.register(PatientData)
class PatientDataAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'AGE', 'GENDER', 'DIABETES', 'DIABETES_TYPE',
        'DIARRHOEA', 'SHORT_STATURE', 'STICKY_STOOL', 'WEIGHT_LOSS',
        'IGA', 'IGG', 'IGM', 'DISEASE_DIAGOSE', 'PROBABILITY'
    )
    list_filter = ('DISEASE_DIAGOSE', 'GENDER', 'DIABETES_TYPE')
    search_fields = ('id',)
