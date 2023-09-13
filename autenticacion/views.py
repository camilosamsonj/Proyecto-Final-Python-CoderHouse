from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import FormularioRegistroUsuarios


def home(request):
    
    return render(request, 'index.html');

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
    
