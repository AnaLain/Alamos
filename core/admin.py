from django.contrib import admin
from .models import Especialidad, Medico, reserva, Paciente, Secretaria, Detalle_Boleta
# Register your models here.

admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(reserva)
admin.site.register(Paciente)
admin.site.register(Secretaria)
admin.site.register(Detalle_Boleta)