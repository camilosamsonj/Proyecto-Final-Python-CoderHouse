from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', home, name='Home'),
    path('registro-usuario', registro, name='Registro'),
    path('login', login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='logout.html', next_page='Registro'), name='Logout'),
    path('editar-perfil', editar_perfil, name='EditarPerfil'),
    path('agregar-avatar', agregarAvatar, name="AgregarAvatar")
    # Otros patrones de URL
]
