# forms.py

from django import forms
from .models import Consulta, Cliente, Doctor

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['cliente', 'doctor', 'fecha_hora', 'notas']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'dni', 'telefono']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad']