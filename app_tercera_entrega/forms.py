from django import forms 
from .models import ItemGasto, CategoriaGasto, MetaAhorro, Contactos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .views import *


class CategoriaGastoFormulario(forms.ModelForm):
   
    class Meta:
        model = CategoriaGasto
        fields = ['nombre', 'descripcion']

class MesAnioWidget(forms.DateInput):
    input_type = 'date'

class ItemGastoFormulario(forms.ModelForm):
    nueva_categoria = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = ItemGasto
        fields = ['nombre', 'monto', 'categoria', 'fecha']
        
    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get('categoria')
        nueva_categoria_nombre = cleaned_data.get('nueva_categoria')
        
        if not categoria and not nueva_categoria_nombre:
            raise forms.ValidationError('Debes seleccionar una categoría o ingresar una nueva')
        
        return cleaned_data
        
    categoria = forms.ModelChoiceField(queryset=CategoriaGasto.objects.all(), empty_label='Selecciona una categoría')
    fecha = forms.DateField(widget=MesAnioWidget)

    
class MetaAhorroFormulario(forms.ModelForm):
        
    class Meta:
        model = MetaAhorro
        fields = ['nombre', 'monto_objetivo', 'fecha_limite']
        
    fecha_limite = forms.DateField(widget=MesAnioWidget)
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        # con esto quitamos los mensajes de ayuda.
        
        help_texts = {k:'' for k in fields}
        
    
class FormularioContactos(forms.ModelForm):
    
    nombre = forms.CharField(max_length=100)
    numero = forms.IntegerField()
    correo = forms.EmailField()
    
    class Meta:
        model = Contactos
        fields = ['nombre', 'numero', 'correo']
                    
        
    

        

