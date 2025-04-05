from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    """ Sirver para poner en puntos la contraseña """
    password = forms.CharField(widget=forms.PasswordInput)