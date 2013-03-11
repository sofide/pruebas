from django.db import models

class Carpeta(models.Model):
    ruta = models.CharField(max_length=200)
    tipo = models.CharField(max_length=7) #valores posibles 'origen' o 'destino'
