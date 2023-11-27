from django.shortcuts import render
from .models import Persona, Visita
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from django import os
from django import time

def is_access_allowed():
    access_interval = int(os.getenv('ACCESS_INTERVAL', 7200))
    last_access_time = int(os.getenv('LAST_ACCESS_TIME', 0))

    current_time = int(time.time())

    if current_time - last_access_time >= access_interval:
        os.environ['LAST_ACCESS_TIME'] = str(current_time)
        return True
    else:
        return False

def lista_Persona(request):
    pass

def detalle_Persona(request, num_exp):
     # Obtener la lista de todos los alumnos desde la base de datos
    Persona = get_object_or_404(Persona, num_exp=num_exp)

    # Pasar la lista de alumnos al template
    return render(request, 'detalle_alumno.html', {'alumno': Persona})

def nueva_visita(request):
    pass
    if Persona.VIP and Persona.acompanado:
        if is_access_allowed:
            return render(request, 'vip_acompanado_pantalla_naranja.html', {'Persona': Persona})
        else:
            return render(request, 'vip_acompanado_pantalla_verde.html', {'Persona': Persona})
    elif Persona.VIP:
        return render(request, 'vip_pantalla_verde.html', {'Persona': Persona})
    elif Persona.acompanado:
        if is_access_allowed:
            return render(request, 'acompanado_pantalla_naranja.html', {'Persona': Persona})
        else:
            return render(request, 'acompanado_pantalla_roja.html', {'Persona': Persona})
    else:
        if is_access_allowed:
            return render(request, 'comunes_pantalla_verde.html', {'Persona': Persona})
        else:
            return render(request, 'comunes_pantalla_roja.html', {'Persona': Persona})
def lista_visitas(request):
    pass