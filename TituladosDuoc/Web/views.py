from .models import Titulado
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import TituladoLoginForm
from .backends import TituladoBackend

def DisenoFirma(request):
    return render(request, '2_DisenoFirma.html')

def Confirmacion(request):
    return render(request, '5_Confirmacion.html')
def custom_login(request):
    if request.method == 'POST':
        form = TituladoLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Utiliza authenticate para verificar las credenciales
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"Usuario {username} autenticado con éxito")
                return redirect('Confirmacion')
            else:
                print("Autenticación fallida")
        else:
            print("Formulario no válido")
    else:
        form = TituladoLoginForm()

    return render(request, 'login.html', {'form': form})


def AsistenciaInvitado(request):
    return render(request, '7_AsistenciaInvitado.html')
