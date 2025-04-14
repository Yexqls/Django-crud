from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from.forms import UserRegistrationForm, UserEditForm, LoginForm, ProfileEditForm
from .models import Profile
from django.contrib import messages
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


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            """ Se encripta la contraseña """
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, 
                                data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                    data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado correctamente', 'succesful')
        else:
            messages.error(request, 'Error al actualizar el perfil', 'error')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', 
                {'user_form': user_form,
                'profile_form': profile_form})