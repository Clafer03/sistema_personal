# models.py

from django.db import models
from django.core.exceptions import ValidationError

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=15, unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.dni})"

class Consulta(models.Model):
    ESTADO_ASISTENCIA = [
        ('pendiente', 'Pendiente'),
        ('asistio', 'Asistió'),
        ('no_asistio', 'No asistió'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    estado_asistencia = models.CharField(max_length=20, choices=ESTADO_ASISTENCIA, default='pendiente')
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.fecha_hora.strftime('%d-%m-%Y %H:%M')} - {self.cliente.nombre}"

    def clean(self):
        conflicto = Consulta.objects.filter(
            doctor=self.doctor,
            fecha_hora=self.fecha_hora
        ).exclude(pk=self.pk).exists()

        if conflicto:
            raise ValidationError("El doctor ya tiene una consulta agendada en ese horario.")
