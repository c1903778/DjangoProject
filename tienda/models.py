from turtle import title
from django.db import models

# Create your models here.
class proyecto(models.Model):
    nombre = models.CharField(max_length = 150)

class tarea(models.Model):
    titulo = models.CharField(max_length = 250)
    descripcion = models.TextField()
    # Crear relacion y a la ves vamos a agregar un elemento 
    proyecto = models.ForeignKey(proyecto, on_delete = models.CASCADE)