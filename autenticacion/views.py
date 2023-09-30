from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import FormularioRegistroUsuarios, UserEditForm
from django.contrib.auth.decorators import login_required
from autenticacion.models import Avatar
from django.contrib.auth.models import User


@login_required
def home(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'index.html', {'url': avatares[0].imagen.url});

def login_request(request):
    if request.method == 'POST':
        #Procesar el formulario de inicio de sesión
        miFormulario = AuthenticationForm(request, data = request.POST)
        if miFormulario.is_valid():
            usuario = miFormulario.cleaned_data.get('username')
            clave = miFormulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'mensaje':f'Bienvenido {usuario}'})
            else: 
                return render(request, 'index.html', {'mensaje': 'Error, datos incorrectos'})        
    else: 
            
        miFormulario = AuthenticationForm()
    return render(request, 'login.html', {'miFormulario': miFormulario})        
            
def registro(request):
    
    if request.method == 'POST':    
        miFormulario = FormularioRegistroUsuarios(request.POST)
        
        if miFormulario.is_valid():
            
            username = miFormulario.cleaned_data['username'] 
            miFormulario.save()
            return render(request, 'inicio.html', {'mensaje': 'Usuario Creado Con Éxito'})    
    else: 
            miFormulario = FormularioRegistroUsuarios()
    return render(request, 'registro.html', {'miFormulario': miFormulario})
   
@login_required 
def editar_perfil(request):
    usuario = request.user # esta es la instancia de la clase User que nos da Django
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            #datos que se modificarán
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return redirect("Inicio")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
    return render(request, 'editar_perfil.html', {"miFormulario": miFormulario, 'usuario':usuario})    