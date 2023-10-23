from django import forms

class TituladoLoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='password')

class ValidarDatosForm(forms.Form):
    rut = forms.CharField(label='rut', max_length=12, required=True)
    num_cedula = forms.CharField(label='num_cedula', max_length=10, required=True)