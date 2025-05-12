from django.db import models

from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=[(0, 'Masculino'), (1, 'Femenino')])
    diabetes = models.BooleanField()
    diabetes_type = models.IntegerField(choices=[(1, 'Tipo 1'), (2, 'Tipo 2'), (3, 'Otro')], null=True, blank=True)
    diarrhoea = models.BooleanField()
    short_stature = models.BooleanField()
    sticky_stool = models.BooleanField()
    weight_loss = models.BooleanField()
    iga = models.FloatField()
    igg = models.FloatField()
    igm = models.FloatField()

    def __str__(self):
        return f"{self.full_name} ({self.age} años)"
