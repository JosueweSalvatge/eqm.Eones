from django.urls import path
from . import views
from .views import lista_alumnos, detalle_alumno, nueva_visita, lista_visitas

urlpatterns = [
    path('', views.lista_alumnos, name='lista_alumnos'),
    path('alumnos/<int:num_exp>/', views.detalle_alumno, name='detalle_alumno'),
    path('visitas/nueva/', views.nueva_visita, name='nueva_visita'),
    path('visitas/', views.lista_visitas, name='lista_visitas'),
]