from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .forms import LoginForm
#Es el controlador y recibe las funciones en este caso el llenado del formulario """
def user_login(request):
    if request.method == 'POST':
         #En caso de ser correcto se recibe todo la informacion del formulario
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #srive para verificar si el usuario existe y la contraseña es correcta
            #si no existe o la contraseña es incorrecta devuelve None
            user = authenticate(request, 
                                username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    #maneja el mensaje en caso de acceso correcto
                    #se puede cambiar por un render a una plantilla
                    login(request, user)
                    return HttpResponse('Usario autenticado')
                else:
                    return HttpResponse('Usuario inactivo')   
            else:
                return HttpResponse('Usuario no encontrado') 
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})