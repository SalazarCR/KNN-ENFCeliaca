from django import forms

class PacienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    sintomas = forms.CharField(widget=forms.Textarea)
