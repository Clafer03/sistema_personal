from django.db import models

class Registro(models.Model):
    fecha = models.DateField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.fecha} - {self.cantidad}"
