from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name='Inicio'),
    path('lista-categorias/', categorias, name='Categorias' ),
    path('formulario-categorias/', formulario_categorias, name='FormularioCategorias' ),
    path('formulario-items/', formulario_items_gastos, name='FormularioItems' ),
    path('formulario-metas/', formulario_meta_ahorro, name='FormularioMetas' ),
    path('busqueda-items/', busqueda_items, name='BusquedaItems' ),
    path('busqueda-items/buscar/', buscar, name='buscar'),
    path('lista-gastos/', lista_gastos, name='ListaGastos'),
    path('login', login_request, name='Login'),
    path('registrar', registro, name='Registro'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('hola-conejo', hola_conejo, name='HolaConejo' ),
    path('formulario-contacto', formulario_contactos, name='FormularioContacto'),
    

]
