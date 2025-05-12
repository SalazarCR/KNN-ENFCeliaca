from django import forms

class CeliacaForm(forms.Form):
    age = forms.IntegerField(label='Edad')
    gender = forms.ChoiceField(label='Género', choices=[(0, 'Masculino'), (1, 'Femenino')])
    diabetes = forms.ChoiceField(label='¿Diabetes?', choices=[(0, 'No'), (1, 'Sí')])
    diabetes_type = forms.ChoiceField(label='Tipo de diabetes', choices=[(0, 'Tipo 1'), (1, 'Tipo 2')])
    diarrhoea = forms.ChoiceField(label='¿Diarrea?', choices=[(0, 'No'), (1, 'Sí')])
    short_stature = forms.ChoiceField(label='¿Estatura baja?', choices=[(0, 'No'), (1, 'Sí')])
    sticky_stool = forms.ChoiceField(label='¿Heces pegajosas?', choices=[(0, 'No'), (1, 'Sí')])
    weight_loss = forms.ChoiceField(label='¿Pérdida de peso?', choices=[(0, 'No'), (1, 'Sí')])
    iga = forms.FloatField(label='IGA')
    igg = forms.FloatField(label='IGG')
    igm = forms.FloatField(label='IGM')
