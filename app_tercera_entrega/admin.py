from django.contrib import admin
from .models import *
from autenticacion.models import Avatar

# Register your models here.

admin.site.register(CategoriaGasto)
admin.site.register(ItemGasto)
admin.site.register(MetaAhorro)
admin.site.register(Avatar)