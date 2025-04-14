from django.contrib import admin
from .models import Profile

""" Se registra el modelo para poder usuarlo """
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Se personaliza el panel de administracion """
    list_display = ['user', 'date_of_birth']
    raw_id_fields = ['user']