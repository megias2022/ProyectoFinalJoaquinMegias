from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_dni = models.IntegerField()
    direccion = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.numero_dni}, {self.direccion},"