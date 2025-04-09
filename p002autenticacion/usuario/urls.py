from django.urls import path
from django.contrib.auth import views as auth_views 
from .import views

#vistas de la aplicacion, las otras uls son del proyecto se puden importar
#unas ya precargadas con django y otras son de la aplicacion
#ya no es necesario crear algunas
urlpatterns = [
    #path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),


]
