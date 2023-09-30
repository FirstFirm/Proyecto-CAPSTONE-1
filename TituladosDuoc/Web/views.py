from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

@login_required
def DisenoLogin(request):
    return render(request, '1_DisenoLogin.html')
def DisenoFirma(request):
    return render(request, '2_DisenoFirma.html')
def Confirmacion(request, username):
    user = User.objects.get(username=username)
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
# Create your views here.
