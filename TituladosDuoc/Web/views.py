from django.shortcuts import render

def DisenoLogin(request):
    return render(request, '1_DisenoLogin.html')
def DisenoFirma(request):
    return render(request, '2_DisenoFirma.html')
def Confirmacion(request):
    return render(request, '5_Confirmacion.html')
def AsistenciaInvitado(request):
    return render(request, '7_AsistenciaInvitado.html')


# Create your views here.
