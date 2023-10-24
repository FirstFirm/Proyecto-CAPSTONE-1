from .models import Titulado
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import TituladoLoginForm, ValidarDatosForm, InvitadoForm
from .backends import TituladoBackend
from django.contrib import messages
from django.contrib.auth import logout


def DisenoFirma(request):
    if request.method == 'POST':
        form = ValidarDatosForm(request.POST)
        if form.is_valid():
            # Obtén el RUT y el número de cédula ingresados en el formulario
            rut_ingresado = form.cleaned_data['rut']
            num_cedula_ingresado = form.cleaned_data['num_cedula']

            # Busca en tu base de datos si existe un RUT y número de cédula válidos
            try:
                registro_valido = Titulado.objects.get(Run=rut_ingresado, NCedula=num_cedula_ingresado)
            except Titulado.DoesNotExist:
                registro_valido = None

            if registro_valido:
                # El RUT y número de cédula son válidos, realiza la acción correspondiente
                # Por ejemplo, podrías redirigir a la página de confirmación
                return redirect('AInvitado')
            else:
                # El RUT o número de cédula no son válidos, muestra un mensaje de error
                messages.error(request, "Los datos ingresados no son válidos. Inténtalo de nuevo.")

    else:
        form = ValidarDatosForm()
    return render(request, '2_DisenoFirma.html')

def Confirmacion(request):
    return render(request, '5_Confirmacion.html')
def resumen(request):
    return render(request, '9_Mensaje.html')
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
                # Agregar un mensaje de error
                messages.error(request, "Los datos ingresados son erróneos. Por favor, inténtalo de nuevo.")
        else:
            print("Formulario no válido")
    else:
        form = TituladoLoginForm()

    return render(request, 'login.html', {'form': form})

def asientos(request):

    titulado = request.user
    return render(request, '6_Asientos.html', {'user': titulado})

def AsistenciaInvitado(request):
    if request.method == 'POST':
        form = InvitadoForm(request.POST)
        if form.is_valid():
            nombre_acompanante1 = form.cleaned_data['nombre_acompanante1']
            nombre_acompanante2 = form.cleaned_data['nombre_acompanante2']

            # Obtén al usuario autenticado (titulado)
            titulado = request.user

            # Actualiza los campos de invitados en el modelo Titulado
            titulado.Invitado1 = nombre_acompanante1
            titulado.Invitado2 = nombre_acompanante2
            titulado.save()

            # Redirige a la siguiente vista, la elección de asientos
            return redirect('Asientos')
    else:
        form = InvitadoForm()

    return render(request, '7_AsistenciaInvitado.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')  # Redirige al usuario a la página de inicio de sesión
