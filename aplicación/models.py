from django.db import models
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    num_exp = models.CharField(max_length=20, unique=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    curs = models.CharField(max_length=50)
    grup = models.CharField(max_length=50)
    vip = models.BooleanField(default=False)
    acomp = models.BooleanField(default=False)
    def _hace_vip (self):
        pass
    def _no_vip (self):
        pass
    def _si_acomp (self):
        pass
    def _no_acomp (self):
        pass

    def __str__(self):
        return self.nombre

class Visitas(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    aceptada = models.BooleanField(default=False)
    alumno = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.alumno.nombre} - {self.fecha_hora}"

