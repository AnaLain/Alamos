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

class Paciente(models.Model):
    rut_pac = models.CharField(max_length=11)
    nombre_pac = models.CharField(max_length=80)
    apaterno_pac = models.CharField(max_length=80)
    amaterno_pac = models.CharField(max_length=80)
    correo_pac = models.EmailField(max_length = 200)
    fecha_nacimiento_pac = models.CharField(max_length=80)
    sexo_pac = models.CharField(max_length=20)
    edad_pac = models.IntegerField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    nombreM = models.ForeignKey(Medico, on_delete=models.CASCADE)

class Secretaria(models.Model):
    rutsec = models.CharField(max_length=11)
    nombre_sec = models.CharField(max_length=80)
    apaterno_sec = models.CharField(max_length=80)
    amaterno_sec = models.CharField(max_length=80)
    correo_sec = models.EmailField(max_length = 200)
    fecha_nacimiento_sec = models.CharField(max_length=80)
    sexo_sec = models.CharField(max_length=20)
    edad_sec = models.IntegerField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    nombreM = models.ForeignKey(Medico, on_delete=models.CASCADE)

class Detalle_Boleta(models.Model):
    nit = models.CharField(max_length=11)
    valor_consulta = models.IntegerField()
    rut_pac = models.CharField(max_length=11)
    fecha_recaudo_boleta = models.CharField(max_length=80)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    nombreM = models.ForeignKey(Medico, on_delete=models.CASCADE)