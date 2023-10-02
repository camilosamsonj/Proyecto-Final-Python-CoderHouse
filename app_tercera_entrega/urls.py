from django.urls import path
from .views import * 





urlpatterns = [
    path('lista-categorias/', categorias, name='Categorias' ),
    path('formulario-categorias/', formulario_categorias, name='FormularioCategorias' ),
    path('formulario-items/', formulario_items_gastos, name='FormularioItems' ),
    # path('formulario-metas/', formulario_meta_ahorro, name='FormularioMetas' ),
    path('busqueda-items/', busqueda_items, name='BusquedaItems' ),
    path('busqueda-items/buscar/', buscar, name='buscar'),
    path('lista-gastos/', lista_gastos, name='ListaGastos'),
    path('about/', about, name="About"),
    path('editar-gasto/<int:pk>/', EditarGasto.as_view(), name="editar_gasto"),
    path('eliminar-gasto/<int:pk>/', EliminarGasto.as_view(), name="eliminar_gasto"),
    path('eliminar-categoria/<int:pk>/', EliminarCategoria.as_view(), name='eliminar_categoria'),
    path('editar-categoria/<int:pk>/', EditarCategoria.as_view(), name='editar_categoria'),
    path('enviar-correo/', enviar_correo, name='enviar_correo')
       
]
