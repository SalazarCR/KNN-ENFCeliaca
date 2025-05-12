from rest_framework import serializers

class PredictionInputSerializer(serializers.Serializer):
    age = serializers.FloatField()
    gender = serializers.FloatField()
    diabetes = serializers.FloatField()
    diabetes_type = serializers.FloatField()
    diarrhoea = serializers.FloatField()
    short_stature = serializers.FloatField()
    sticky_stool = serializers.FloatField()
    weight_loss = serializers.FloatField()
    iga = serializers.FloatField()
    igg = serializers.FloatField()
    igm = serializers.FloatField()
