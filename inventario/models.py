from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre_producto = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    descripcion = models.TextField()
