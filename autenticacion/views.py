from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import FormularioRegistroUsuarios, UserEditForm
from django.contrib.auth.decorators import login_required
from autenticacion.models import *
from django.contrib.auth.models import User
from .forms import AvatarFormulario


def home(request):
    
    usuario_actual = request.user
    avatares = Avatar.objects.filter(user=request.user.id) 
    
    if avatares.exists():
        url_avatar = avatares[0].imagen.url
    else: 
        url_avatar = None
        
    return render(request, 'index.html', {'url_avatar': url_avatar, 'usuario_actual': usuario_actual});

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
                return redirect("Home")
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
            return redirect("Home")    
    else: 
            miFormulario = FormularioRegistroUsuarios()
    return render(request, 'registro.html', {'miFormulario': miFormulario})
   

@login_required 
def editar_perfil(request):
    usuario = request.user # esta es la instancia de la clase User que nos da Django
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            #datos que se modificarán
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return redirect("Home")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
    return render(request, 'editar_perfil.html', {"miFormulario": miFormulario, 'usuario':usuario})    



def agregarAvatar(request):
    
    if request.method == 'POST':
        
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            
            avatar = Avatar(user=request.user, imagen=data['imagen'])
            avatar.save()
            
            return redirect("Home") 
        
        # else:
            
        #     return render(request, 'Home')
    
    else: 
        miFormulario= AvatarFormulario()
        
    return render(request, 'agregar_avatar.html', {'miFormulario': miFormulario})