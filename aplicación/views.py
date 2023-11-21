from django.shortcuts import render
from .models import Persona, Visitas
from django.shortcuts import render, get_object_or_404


def lista_alumnos(request):
    pass

def detalle_alumno(request, num_exp):
     # Obtener la lista de todos los alumnos desde la base de datos
    alumno = get_object_or_404(Persona, num_exp=num_exp)

    # Pasar la lista de alumnos al template
    return render(request, 'detalle_alumno.html', {'alumno': alumno})

def nueva_visita(request):
    pass

def lista_visitas(request):
    pass