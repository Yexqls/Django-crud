from django.db import models
from django.conf import settings

class Profile(models.Model):
    """ El modelo creado tiene como base el modelo usuario """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    """ Sirve para debuguear errores """
    def __str__(self):
        return f'Perfil de{self.user.username}'