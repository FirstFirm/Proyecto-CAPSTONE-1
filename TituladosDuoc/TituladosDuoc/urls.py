"""
URL configuration for TituladosDuoc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path, include
from Web.views import DisenoLogin, DisenoFirma, Confirmacion, AsistenciaInvitado, login_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DisenoLogin, name='login'),
    path('Diseño_firma', DisenoFirma, name='firma'),
    path('Confirmacion', Confirmacion, name='Confirmacion'),
    path('AsistenciaInvitado', AsistenciaInvitado, name='AInvitado'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login_view, name='login'),  # URL de inicio de sesión personalizada
    #path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL de cierre de sesión de Django
]
