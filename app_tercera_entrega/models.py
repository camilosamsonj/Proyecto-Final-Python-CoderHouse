from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CategoriaGasto(models.Model):
    
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Agrega este campo

    
    def __str__(self):
        return f'{self.nombre}'

class ItemGasto(models.Model):
    
    nombre = models.CharField(max_length=100)
    monto = models.IntegerField()
    categoria = models.ForeignKey(CategoriaGasto, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class MetaAhorro(models.Model):
    nombre = models.CharField(max_length=100)
    monto_objetivo = models.IntegerField()
    fecha_limite = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

    