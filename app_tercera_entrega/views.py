from typing import Any
from .forms import *
from django.http import HttpResponse
from django.views.generic import View, CreateView, TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView 
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required   
from django.urls import reverse_lazy
from django.core.mail import send_mail


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




@login_required
def formulario_items_gastos(request):
    if request.method == 'POST':
        miFormulario = ItemGastoFormulario(request.POST)
        
        try:
            if miFormulario.is_valid():
                datos_formulario = miFormulario.cleaned_data
                nueva_categoria_nombre = datos_formulario.get('nueva_categoria')

                if nueva_categoria_nombre:
                    nueva_categoria, created = CategoriaGasto.objects.get_or_create(
                        nombre=nueva_categoria_nombre,
                        usuario=request.user
                    )
                    item_gasto = ItemGasto.objects.create(
                        nombre=datos_formulario['nombre'],
                        monto=datos_formulario['monto'],
                        categoria=nueva_categoria,
                        fecha=datos_formulario['fecha'],
                        usuario=request.user
                    )
                else:
                    categoria = datos_formulario['categoria']
                    item_gasto = ItemGasto.objects.create(
                        nombre=datos_formulario['nombre'],
                        monto=datos_formulario['monto'],
                        categoria=categoria,
                        fecha=datos_formulario['fecha'],
                        usuario=request.user
                    )

                return redirect("ListaGastos")

        except CategoriaGasto.DoesNotExist:
            # Aquí, si la categoría no existe, deberías manejarlo de alguna manera,
            # por ejemplo, redirigiendo a una página de error.
            return redirect("error_categorias")

    else:
        miFormulario = ItemGastoFormulario()

    return render(request, 'formulario_items_gastos.html', {'miFormulario': miFormulario})


@login_required
def categorias(request):
    
    categorias = CategoriaGasto.objects.all()
    
    return render(request, 'lista_categorias.html', {'lista_categorias': categorias})

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

# class ListadoGastos(TemplateView):
#     template_name = 'lista_gastos.html'
    
#     def get(self, request, *args, **kwargs):
#         gastos = ItemGasto.objects.filter(usuario=request.user )
#         return render(request, self.template_name, {'gastos': gastos })


def about(request):
    
    return render(request, 'about.html')


class EditarGasto(UpdateView):
    model = ItemGasto
    template_name = 'editar_gasto.html'
    form_class = ItemGastoForm
    success_url = reverse_lazy('ListaGastos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gasto'] = self.get_object
        return context
class EliminarGasto(DeleteView):
    model = ItemGasto
    template_name = 'eliminar_gasto.html'
    success_url = reverse_lazy('ListaGastos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gasto'] = self.get_object
        return context
class EliminarCategoria(DeleteView):
    model = CategoriaGasto
    template_name = 'eliminar_categoria.html'
    success_url = reverse_lazy('Categorias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.get_object
        return context
class EditarCategoria(UpdateView):
    
    model = CategoriaGasto
    template_name = 'editar_categoria.html'
    form_class = EditCategoriaForm
    success_url = reverse_lazy('Categorias')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.get_object
        return context
    
    
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm  # Asegúrate de tener tu formulario en forms.py

def enviar_correo(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y enviar el correo electrónico
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']

            subject = f'Mensaje de contacto de {nombre}'
            message = f'Correo de contacto: {correo}\n\nMensaje:\n{mensaje}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]  # Puedes configurar esta dirección en settings.py

            send_mail(subject, message, from_email, recipient_list)

            # Puedes redirigir a una página de éxito o mostrar un mensaje de éxito aquí
            return redirect('exito')

    else:
        form = ContactForm()

    return render(request, 'formulario_contacto.html', {'form': form})
