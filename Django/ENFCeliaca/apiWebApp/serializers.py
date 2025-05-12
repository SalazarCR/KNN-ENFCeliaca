from rest_framework import serializers

class CeliacaPredictionSerializer(serializers.Serializer):
    AGE = serializers.FloatField()
    GENDER = serializers.FloatField()
    DIABETES = serializers.FloatField()
    DIARRHOEA = serializers.FloatField()
    SHORT_STATURE = serializers.FloatField()
    STICKY_STOOL = serializers.FloatField()
    WEIGHT_LOSS = serializers.FloatField()
    IGA = serializers.FloatField()
    IGG = serializers.FloatField()
    IGM = serializers.FloatField()
    DISEASE_DIAGNOSE = serializers.IntegerField()  # Este es el atributo a predecir
    # Si deseas que el atributo 'DISEASE_DIAGNOSE' también sea parte de la entrada,
    # lo mantienes como lo has hecho. Si solo es una predicción, lo eliminarás de la entrada.
