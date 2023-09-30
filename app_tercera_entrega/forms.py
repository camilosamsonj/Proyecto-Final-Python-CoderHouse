from django import forms 
from .models import ItemGasto, CategoriaGasto, MetaAhorro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .views import *


class CategoriaGastoFormulario(forms.ModelForm):
   
    class Meta:
        model = CategoriaGasto
        fields = ['nombre', 'descripcion']
    
    nombre = forms.CharField(widget=forms.TextInput(), label='Nombre', initial='')
    descripcion = forms.CharField(widget=forms.TextInput(), label='Descripcion', initial='')

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtén las categorías desde la base de datos y conviértelas en una lista de opciones
        categorias = [(categoria.id, categoria.nombre) for categoria in CategoriaGasto.objects.all()]
        # Agrega una opción inicial para que el usuario la seleccione
        categorias.insert(0, ('', 'Selecciona una categoría'))
        # Establece las opciones en el campo "categoria"
        self.fields['categoria'].choices = categorias

    nombre = forms.CharField(widget=forms.TextInput(), label='Nombre del gasto', initial='')
    monto = forms.CharField(widget=forms.NumberInput(), label='Monto', initial='')    
    categoria = forms.ModelChoiceField(queryset=CategoriaGasto.objects.all(), empty_label='Selecciona una categoría')
    fecha = forms.DateField(widget=MesAnioWidget)
   

    
class MetaAhorroFormulario(forms.Form):
    
    class Meta:
        model: MetaAhorro
        fields = ['nombre', 'monto_objetivo','fecha_limite', 'usuario']

    nombre = forms.CharField(widget=forms.TextInput(), label='Nombre', initial='')
    monto_objetivo = forms.CharField(widget=forms.TextInput(), label='Objetivo', initial='')
    fecha_limite = forms.CharField(widget=MesAnioWidget(), label='Fecha Límite', initial='')

                    
        
    

        

