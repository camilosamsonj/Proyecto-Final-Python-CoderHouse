from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import CategoriaGastoFormulario, ItemGastoFormulario, MetaAhorroFormulario
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# def inicio(request):
#     usuario_actual = request.user
#     return render(request, "inicio.html", {'usuario_actual': usuario_actual})

@login_required 
def formulario_categorias(request):

    
    if request.method == 'POST':
        
        miFormulario = CategoriaGastoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            datos_formulario = miFormulario.cleaned_data
            usuario = request.user
            categoria = CategoriaGasto(nombre=datos_formulario['nombre'], descripcion=datos_formulario['descripcion'], usuario=usuario ) # Asociamos la categoria de gasto al usuario actual
            categoria.save()
            return redirect("Categorias")
            
        
    else:
        
        miFormulario = CategoriaGastoFormulario()
    
    return render(request, 'formulario_categorias.html', {'miFormulario': miFormulario})




@login_required # Con esto nos aseguramos que el usuario esté autenticado
def formulario_items_gastos(request):

    
    if request.method == 'POST':
        
        miFormulario = ItemGastoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            datos_formulario = miFormulario.cleaned_data
            nueva_categoria_nombre = datos_formulario.get('nueva_categoria')
            
            if nueva_categoria_nombre:
                nueva_categoria = CategoriaGasto(nombre=nueva_categoria_nombre, usuario=request.user)
                nueva_categoria.save()

            
            categoria = miFormulario.cleaned_data['categoria']
            
            item_gasto = ItemGasto(
            nombre=datos_formulario['nombre'],
            monto=datos_formulario['monto'],
            categoria=categoria,  # Asociar el item a la categoría seleccionada
            fecha=datos_formulario['fecha'], usuario=request.user
            )
            item_gasto.save()
            return redirect("ListaGastos")
        
        
    else:
        
        miFormulario = ItemGastoFormulario()
    
    return render(request, 'formulario_items_gastos.html', {'miFormulario': miFormulario})

@login_required
def categorias(request):
    
    categorias = CategoriaGasto.objects.all()
    
    return render(request, 'lista_categorias.html', {'lista_categorias': categorias})


@login_required
def formulario_meta_ahorro(request):

    
    if request.method == 'POST':
        miFormulario = MetaAhorroFormulario(request.POST)
        if miFormulario.is_valid():
            datos_formulario = miFormulario.cleaned_data
            usuario = request.user 
            meta_ahorro = MetaAhorro(nombre=datos_formulario['nombre'], monto_objetivo=datos_formulario['monto_objetivo'], fecha_limite=datos_formulario['fecha_limite'], usuario = usuario)
            meta_ahorro.save()
            return redirect("ListaGastos")
        
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



@login_required
def lista_gastos(request):
    
    if request.user.is_authenticated:
            
        gastos = ItemGasto.objects.filter(usuario=request.user)
    
    else: 
        gastos = [] 
        
    return render(request, 'lista_gastos.html', {'gastos': gastos})

    
