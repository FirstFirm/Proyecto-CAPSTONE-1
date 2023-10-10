from django import forms

class TituladoLoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='password')