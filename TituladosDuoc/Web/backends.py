from django.contrib.auth.backends import BaseBackend
from .models import Titulado

class TituladoBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            username = Titulado.objects.get(username=username)
            if username.password == password:
                return username
        except Titulado.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Titulado.objects.get(pk=user_id)
        except Titulado.DoesNotExist:
            return None
