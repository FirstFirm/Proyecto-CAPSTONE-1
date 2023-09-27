from django.contrib import admin
from .models import Titulado

class TituladoAdmin(admin.ModelAdmin):
    list_display = ('Run', 'Nombres', 'ApellidoP', 'ApellidoM', 'NCeluda', 'Celular', 'Email',
                    'Contrasena', 'Carrera', 'Codigo', 'Invitado1', 'Invitado2')

# Registrar el modelo Titulado con la clase personalizada TituladoAdmin
admin.site.register(Titulado, TituladoAdmin)