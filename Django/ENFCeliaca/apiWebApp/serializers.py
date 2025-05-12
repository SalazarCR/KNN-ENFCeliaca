from rest_framework import serializers

class CeliacaPredictionSerializer(serializers.Serializer):
    # Asegúrate de que los campos coincidan con los del formulario de datos
    AGE = serializers.IntegerField()
    GENDER = serializers.BooleanField()  # 1 o 0
    DIABETES = serializers.BooleanField()  # 1 o 0
    DIARRHOEA = serializers.IntegerField()  # 0, 1, 2
    SHORT_STATURE = serializers.BooleanField()  # 1 o 0
    STICKY_STOOL = serializers.BooleanField()  # 1 o 0
    WEIGHT_LOSS = serializers.FloatField()
    IGA = serializers.FloatField()
    IGG = serializers.FloatField()
    IGM = serializers.FloatField()
