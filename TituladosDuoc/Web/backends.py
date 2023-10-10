from django.contrib.auth.backends import BaseBackend
from .models import Titulado

class TituladoBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Titulado.objects.get(username=username)
            if user.password == password:
                return user
        except Titulado.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Titulado.objects.get(pk=user_id)
        except Titulado.DoesNotExist:
            return None
