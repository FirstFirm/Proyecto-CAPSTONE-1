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
    Carrera = models.CharField(max_length=50)
    CodigoAsiento = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    Invitado1 = models.CharField(max_length=50, null=True, blank=True)
    Invitado2 = models.CharField(max_length=50, null=True, blank=True)

def __str__(self):
    return f"{self.Nombres} {self.ApellidoP} {self.ApellidoM}"
@receiver(post_save, sender=User)
def create_or_update_titulado(sender, instance, created, **kwargs):
    # Utiliza get_or_create para obtener o crear el objeto Titulado
    titulado, created = Titulado.objects.get_or_create(usuario=instance)

