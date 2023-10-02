from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .views import *
from django import forms 
from .models import Avatar


class MesAnioWidget(forms.DateInput):
    input_type = 'date'

class FormularioRegistroUsuarios(UserCreationForm):
    
    email = forms.EmailField(label="Correo Electrónico", widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu correo electrónico' }))
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña' }))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Repite tu contraseña'}))
    
    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']
          
        help_texts = {k:"" for k in fields}
        
    # Personalizar la etiqueta del campo "username"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar e-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, initial='')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput, initial='')
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ('imagen',)
    
 

       
    