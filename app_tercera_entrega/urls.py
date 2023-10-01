from django.urls import path
from .views import *




urlpatterns = [
    path('lista-categorias/', categorias, name='Categorias' ),
    path('formulario-categorias/', formulario_categorias, name='FormularioCategorias' ),
    path('formulario-items/', formulario_items_gastos, name='FormularioItems' ),
    path('formulario-metas/', formulario_meta_ahorro, name='FormularioMetas' ),
    path('busqueda-items/', busqueda_items, name='BusquedaItems' ),
    path('busqueda-items/buscar/', buscar, name='buscar'),
    path('lista-gastos/', lista_gastos, name='ListaGastos'),
       

]
