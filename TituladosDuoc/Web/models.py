import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Titulado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    Run = models.CharField(max_length=11, unique=True, default=0)
    Nombres = models.CharField(max_length=50)
    ApellidoP = models.CharField(max_length=50)
    ApellidoM = models.CharField(max_length=50)
    NCeluda = models.CharField(max_length=10)
    Celular = models.CharField(max_length=10)
    Email = models.EmailField(unique=True)
    Carrera = models.CharField(max_length=50)
    Codigo = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    Invitado1 = models.CharField(max_length=50, null=True, blank=True)
    Invitado2 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre
@receiver(post_save, sender=User)
def create_titulado(sender, instance, created, **kwargs):
    if created:
        Titulado.objects.create(usuario=instance)
