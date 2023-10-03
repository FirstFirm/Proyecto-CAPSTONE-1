from django.db import models

# Create your models here.
class Titulado(models.Model):
    Run = models.CharField(max_length=11, unique=True)
    Nombres = models.CharField(max_length=50)
    ApellidoP = models.CharField(max_length=50)
    ApellidoM = models.CharField(max_length=50)
    NCeluda = models.CharField(max_length=10)
    Celular = models.CharField(max_length=10)
    Email = models.EmailField(unique=True)
    Contrasena = models.CharField(max_length=50)
    Carrera = models.CharField(max_length=50)
    Codigo = models.IntegerField(unique=True)
    Invitado1 = models.CharField(max_length=50, null=True, blank=True)
    Invitado2 = models.CharField(max_length=50, null=True, blank=True)
    #Quedé en asociar un usuario de django a un modelo