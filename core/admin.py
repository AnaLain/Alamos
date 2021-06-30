from django.contrib import admin
from .models import Especialidad, Medico, reserva
# Register your models here.

admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(reserva)