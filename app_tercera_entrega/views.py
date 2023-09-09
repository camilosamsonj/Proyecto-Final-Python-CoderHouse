from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import CategoriaGastoFormulario, ItemGastoFormulario, MetaAhorroFormulario, UserRegisterForm, FormularioContactos
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

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
            return redirect("Categorias")
            
        
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
            return redirect("ListaGastos")
        
        
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




def lista_gastos(request):
    
    gastos = ItemGasto.objects.all()
    
    return render(request, 'lista_gastos.html', {'gastos': gastos})


def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            
            if user is not None:
                login(request, user)
                
                messages.success(request, f'Bienvenido {usuario}')
                return render(request, 'inicio.html', {})
            
            else: 
                return render(request, 'inicio.html', {'mensaje':'Error datos incorrectos'})
        
        else:
            return render(request, 'inicio.html', {'mensaje': 'Error, formulario erróneo'})
        
    else:
        
        form = AuthenticationForm()
        
        return render(request, 'login.html', {'form':form})
    


def registro(request):
    
    if request.method == 'POST':
        
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleanead_data['username']
            form.save()
            return render(request, 'inicio.html', {'mensaje': 'Usuario Creado Con Éxito'})
        
    else: 
            # form = UserCreationForm()
            form = UserRegisterForm()
            
    return render(request, 'registro.html', {'form': form})
    
    
def hola_conejo(request):
    
  return render(request, 'hola_conejo.html')


def formulario_contactos(request):
    
    if request.method == 'POST':
        
        miFormulario = FormularioContactos(request.POST)
        
        if miFormulario.is_valid():
            
            datos_formulario = miFormulario.cleaned_data
            contacto = Contactos(nombre=datos_formulario['nombre'], numero=datos_formulario['numero'], correo=datos_formulario['correo'])
            contacto.save()
            return redirect("FormularioContacto")
        
    else:
        
        miFormulario = FormularioContactos()
    
    return render(request, 'formulario_contactos.html', {'miFormulario': miFormulario})