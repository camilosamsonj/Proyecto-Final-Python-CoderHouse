from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='Home'),
    path('registro-usuario', registro, name='Registro'),
    path('login', login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='logout.html', next_page='Registro'), name='Logout'),
    
    # Otros patrones de URL
]