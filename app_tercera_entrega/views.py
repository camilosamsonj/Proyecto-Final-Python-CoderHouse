from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *


# Create your views here.
def inicio(request):

    return render(request, "inicio.html")


def formulario_categorias(request):

    
    if request.method == 'POST':
        
        miFormulario = CategoriaGastoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            datos_formulario = miFormulario.cleaned_data
            categoria = CategoriaGasto(nombre=datos_formulario['nombre'], descripcion=datos_formulario['descripcion'])
            categoria.save()
            return render(request, "lista_categorias.html")
        
    else:
        
        miFormulario = CategoriaGastoFormulario()
    
    return render(request, 'formulario_categorias.html', {'miFormulario': miFormulario})


def formulario_items_gastos(request):

    
    if request.method == 'POST':
        
        miFormulario = ItemGastoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            datos_formulario = miFormulario.cleaned_data
            nueva_categoria_nombre = datos_formulario.get('nueva_categoria')
            
            if nueva_categoria_nombre:
                nueva_categoria = CategoriaGasto(nombre=nueva_categoria_nombre)
                nueva_categoria.save()

            
            categoria = miFormulario.cleaned_data['categoria']
            
            item_gasto = ItemGasto(
            nombre=datos_formulario['nombre'],
            monto=datos_formulario['monto'],
            categoria=categoria,  # Asociar el item a la categoría seleccionada
            fecha=datos_formulario['fecha']
            )
            item_gasto.save()
            return render(request, "lista_categorias.html")
        
        
    else:
        
        miFormulario = ItemGastoFormulario()
    
    return render(request, 'formulario_items_gastos.html', {'miFormulario': miFormulario})


def categorias(request):
    
    categorias = CategoriaGasto.objects.all()
    
    return render(request, 'lista_categorias.html', {'lista_categorias': categorias})



def formulario_meta_ahorro(request):

    
    if request.method == 'POST':
        
        miFormulario = MetaAhorroFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            datos_formulario = miFormulario.cleaned_data
            meta_ahorro = MetaAhorro(nombre=datos_formulario['nombre'], monto_objetivo=datos_formulario['monto_objetivo'], fecha_limite=datos_formulario['fecha_limite'])
            meta_ahorro.save()
            return render(request, "inicio.html")
        
    else:
        
        miFormulario = MetaAhorroFormulario()
    
    return render(request, 'formulario_metas.html', {'miFormulario': miFormulario})


def busqueda_items(request):
    
    return render(request, 'busqueda_items.html')

def buscar(request):
    
    if request.GET['item']:
        
        item = request.GET['item']
        resultados = ItemGasto.objects.filter(nombre__icontains=item)
        
        return render(request, 'resultado_busqueda.html', {'resultados': resultados, 'item_nombre': item})
    
    else: 
        respuesta = "No enviaste los datos"
    
    return HttpResponse(respuesta)




# def gastos_por_categorias(request):
    
#     categorias = CategoriaGasto.objects.all()
    
#     return render(request, 'lista_categorias.html', {'lista_categorias': categorias})
