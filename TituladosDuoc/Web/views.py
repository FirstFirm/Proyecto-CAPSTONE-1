from .models import Titulado
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models.signals import post_save


@login_required
def DisenoLogin(request):
    return render(request, '1_DisenoLogin.html')
def DisenoFirma(request):
    return render(request, '2_DisenoFirma.html')
def Confirmacion(request):
    user = request.user  # Obtiene el usuario autenticado
    context = {'user': user}
    return render(request, '5_Confirmacion.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            # Redirigir al usuario a la página de confirmación
            return redirect('Confirmacion', username=user.username)
        else:
            # Handle invalid login credentials
            pass
    return render(request, '5_Confirmacion.html')

def AsistenciaInvitado(request):
    return render(request, '7_AsistenciaInvitado.html')
@receiver(post_save, sender=User)
def create_titulado(sender, instance, created, **kwargs):
    if created:
        Titulado.objects.create(usuario=instance)

# Create your views here.
