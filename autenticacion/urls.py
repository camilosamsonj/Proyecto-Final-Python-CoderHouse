from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='Home'),
    path('registro-usuario', registro, name='Registro'),
    path('login', login_request, name='Login'),
    
    # Otros patrones de URL
]