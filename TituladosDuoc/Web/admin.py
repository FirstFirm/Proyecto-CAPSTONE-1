from django.contrib import admin
from .models import Titulado

class TituladoAdmin(admin.ModelAdmin):
    list_display = ('username' ,'password','Run', 'NCedula',
                    'Carrera', 'NAsiento', 'Invitado1', 'Invitado2')

# Registrar el modelo Titulado con la clase personalizada TituladoAdmin
admin.site.register(Titulado, TituladoAdmin)