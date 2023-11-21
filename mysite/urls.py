from django.urls import path
from .views import lista_alumnos, detalle_alumno, nueva_visita, lista_visitas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion.urls')),
]



