from django.db import models
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy


# Create your models here.
class Productos (models.Model):
    nombre = models.CharField (max_length=150)
    modelo = models.CharField (max_length=150, blank=True , null=True)
    precio = models.IntegerField (default=0)
    imagen = models.ImageField (upload_to = "productos", null = True, blank = True)
    Stock = models.FloatField(default=0)
    info = models.CharField(max_length=1500, default=0)
    fecha = models.DateField(db_column= 'fecha', blank= True, null = True)

    

    def __str__(self):
        return f"{self.nombre} - {self.modelo} - {self.precio} - {self.imagen}"

class Integrantes (models.Model):
    nombre = models.CharField (max_length=150)
    edad = models.IntegerField ()
    profesion = models.CharField(max_length=150)
    
    def __str__(self):
     return f"informacion de {self.nombre} - {self.edad} - {self.profesion}"

class Sucursales (models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    dias = models.CharField(max_length=150)
    horarios = models.CharField(max_length=150) 

    def __str__(self):
     return f"Sucursal {self.nombre}"








