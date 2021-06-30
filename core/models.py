from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(max_length=80)

def __str__(self):
        return self.especialidad

class Medico(models.Model):
    rut = models.CharField(max_length=11)
    nombreM = models.CharField(max_length=80)
    apaterno = models.CharField(max_length=80)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
def __str__(self):
        return self.rut
def __str__(self):
        return self.apaterno
def __str__(self):
        return self.nombreM    

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
def __str__(self):
        return self.rut
def __str__(self):
        return self.nombre
def __str__(self):
        return self.apaterno
def __str__(self):
        return self.correo
def __str__(self):
        return self.fecha_nacimiento    
    
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
def __str__(self):
        return self.rut_pac
def __str__(self):
        return self.nombre_pac
def __str__(self):
        return self.apaterno_pac
def __str__(self):
        return self.amaterno_pac

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
def __str__(self):
        return self.rut_sec
def __str__(self):
        return self.nombre_sec
def __str__(self):
        return self.apaterno_sec
def __str__(self):
        return self.amaterno_sec

class Detalle_Boleta(models.Model):
    nit = models.CharField(max_length=11)
    valor_consulta = models.IntegerField()
    rut_pac = models.CharField(max_length=11)
    fecha_recaudo_boleta = models.CharField(max_length=80)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    nombreM = models.ForeignKey(Medico, on_delete=models.CASCADE)
def __str__(self):
        return self.nit
def __str__(self):
        return self.valor_consulta
def __str__(self):
        return self.fecha_recaudo_boleta    