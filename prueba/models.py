from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=100)
class libro(models.Model):
    nombre = models.CharField(max_length=100)