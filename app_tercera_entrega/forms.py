from django import forms 
from .models import ItemGasto, CategoriaGasto
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

    nombre = forms.CharField(label='Nombre del gasto', initial='')
    monto = forms.CharField(label='Monto', initial='')    
    categoria = forms.ModelChoiceField(
        queryset=CategoriaGasto.objects.all(), 
        empty_label='Selecciona una categoría existente', 
        required=False
        )
    fecha = forms.DateField(widget=MesAnioWidget)

class ItemGastoForm(forms.ModelForm):
    class Meta:
        model = ItemGasto
        fields = ['nombre', 'monto', 'categoria', 'fecha']

class EditCategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaGasto
        fields = ['nombre', 'descripcion']


class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo electrónico')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)