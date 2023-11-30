from django.shortcuts import render
from django import Persona, Visitas
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta


def lista_alumno(request):
    pass

def detalle_alumno(request, num_exp):
     # Obtener la lista de todos los alumnos desde la base de datos
    Persona = get_object_or_404(Persona, num_exp=num_exp)

    # Pasar la lista de alumnos al template
    return render(request, 'detalle_alumno.html', {'alumno': Persona})

def nueva_visita(request):
    try:
        tiempo_anterior = datetime()  # Formato: Año, Mes, Día, Hora, Minuto, Segundo
    except:
         tiempo_anterior = datetime(2001, 1, 1, 1, 1, 1)
         
    tiempo_actual = datetime.now()  # Tiempo actual
    diferencia = tiempo_actual - tiempo_anterior
    if Persona.VIP and Persona.acompanado:
        if diferencia > timedelta(hours=2):
            return render(request, 'vip_acompanado_pantalla_naranja.html', {'Persona': Persona})
        else:
            return render(request, 'vip_acompanado_pantalla_verde.html', {'Persona': Persona})
    elif Persona.VIP:
        return render(request, 'vip_pantalla_verde.html', {'Persona': Persona})
    elif Persona.acompanado:
        if diferencia > timedelta(hours=2):
            return render(request, 'acompanado_pantalla_naranja.html', {'Persona': Persona})
        else:
            return render(request, 'acompanado_pantalla_roja.html', {'Persona': Persona})
    else:
        if diferencia > timedelta(hours=2):
            return render(request, 'comunes_pantalla_verde.html', {'Persona': Persona})
        else:
            return render(request, 'comunes_pantalla_roja.html', {'Persona': Persona})
        