from django.db import models

# Create your models here.
class registros(models.Model):
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    usuario = models.CharField(max_length=12)
    pais = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    postal= models.IntegerField()