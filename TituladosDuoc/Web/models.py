import uuid
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Titulado(AbstractUser):
    username = models.CharField(max_length=100, unique=True, default='NombreUsuario')
    password = models.CharField(max_length=128, default='titulados')
    Run = models.CharField(max_length=11)
    NCeluda = models.CharField(max_length=10)
    Carrera = models.CharField(max_length=50)
    NAsiento = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    Invitado1 = models.CharField(max_length=50, null=True, blank=True)
    Invitado2 = models.CharField(max_length=50, null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True, null=True, blank=True)
    backend = 'Web.backends.TituladoBackend'  # Reemplaza 'myapp' con la ubicación real de tu aplicación y el backend personalizado

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='titulado_set',
        related_query_name='titulado',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='titulado_set',
        related_query_name='titulado',
    )

    def save(self, *args, **kwargs):
        # Hashear la contraseña antes de guardarla
        self.password = make_password(self.password)
        super().save(*args, **kwargs)