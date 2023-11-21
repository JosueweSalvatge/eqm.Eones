from django.urls import path
from .views import lista_alumnos, detalle_alumno, nueva_visita, lista_visitas

urlpatterns = [
    path('', lista_alumnos, name='lista_alumnos'),
    path('alumnos/<int:num_exp>/', detalle_alumno, name='detalle_alumno'),
    path('visitas/nueva/', nueva_visita, name='nueva_visita'),
    path('visitas/', lista_visitas, name='lista_visitas'),
]