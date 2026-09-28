from django.db import models

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()
    fecha_salida = models.DateField()
    categoria = models.CharField(max_length=50)
