from django.db import models
from django.utils import timezone


class CategoriaGasto(models.Model):
    
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    
    def __str__(self):
        return f'Categoría: {self.nombre}'

class ItemGasto(models.Model):
    
    nombre = models.CharField(max_length=100)
    monto = models.IntegerField()
    categoria = models.ForeignKey(CategoriaGasto, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nombre


class MetaAhorro(models.Model):
    nombre = models.CharField(max_length=100)
    monto_objetivo = models.IntegerField()
    fecha_limite = models.DateField()
        
    
    
