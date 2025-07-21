from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['fecha', 'cantidad']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'cantidad': forms.NumberInput(attrs={'min': 0}),
        }
        labels = {
            'fecha': 'Fecha',
            'cantidad': 'Cantidad',
        }