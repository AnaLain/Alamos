from django.shortcuts import render, redirect
from .models import Especialidad,Medico, reserva

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def diario(request):
    return render(request, 'core/diario.html')

def homepacientes(request):

    especialidad , medico = Especialidad.objects.all, Medico.objects.all 

    variables = {
        'especialidad': especialidad,
        'medico': medico
    }

    if request.POST:
        Reserva = reserva()
        Reserva.rut = request.POST.get('rut')
        Reserva.nombre = request.POST.get('nombre')
        Reserva.apaterno = request.POST.get('paterno')
        Reserva.amaterno = request.POST.get('materno')
        Reserva.correo = request.POST.get('correo')
        Reserva.fecha_nacimiento = request.POST.get('fechaNacimiento')
        Reserva.sexo = request.POST.get('sexo')
        especialidad = Especialidad
        Especialidad.id = request.POST.get('especialidad')
        medico = Medico()
        Medico.id = request.POST.get('servicio')
        Reserva.montoR = request.POST.get('monto')
        Reserva.fecha_reservaR = request.POST.get('fecha')
        Reserva.horaR = request.POST.get('hora')
        try:
            Reserva.save()
            variables['mensaje'] = 'guardado correcctamente'
        except:
            variables['mensaje'] = 'error al guardar'
            
    return render(request, 'core/homepacientes.html',variables)
    

def login_medico(request):
    return render(request, 'core/login_medico.html')

def login_secretaria(request):
    return render(request, 'core/login_secretaria.html')

def vistamedico(request):
    return render(request, 'core/vistamedico.html')

def paciente(request):
    return render(request, 'core/paciente.html')

def recaudo(request):
    return render(request, 'core/recaudo.html')

def total(request):
    return render(request, 'core/total.html')
