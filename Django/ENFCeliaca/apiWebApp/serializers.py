from rest_framework import serializers

class CeliacaPredictionSerializer(serializers.Serializer):
    AGE = serializers.IntegerField()
    GENDER = serializers.CharField(max_length=10)
    DIABETES = serializers.BooleanField()
    DIARRHOEA = serializers.BooleanField()
    SHORT_STATURE = serializers.BooleanField()
    STICKY_STOOL = serializers.BooleanField()
    WEIGHT_LOSS = serializers.BooleanField()
    IGA = serializers.FloatField()
    IGG = serializers.FloatField()
    IGM = serializers.FloatField()
    DISEASE_DIAGNOSE = serializers.IntegerField()
