from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=80)

class Medico(models.Model):
    rut = models.CharField(max_length=11)
    nombreM = models.CharField(max_length=80)
    apaterno = models.CharField(max_length=80)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

class reserva(models.Model):
    rut = models.CharField(max_length=11)
    nombre = models.CharField(max_length=80)
    apaterno = models.CharField(max_length=80)
    amaterno = models.CharField(max_length=80)
    correo = models.EmailField(max_length = 200)
    fecha_nacimiento = models.CharField(max_length=80)
    sexo = models.CharField(max_length=20)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    nombreM = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_reservaR = models.CharField(max_length=80)
    montoR = models.FloatField()
    horaR = models.CharField(max_length=80)



