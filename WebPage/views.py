from django.http import HttpResponse
from django.shortcuts import render, redirect
from WebPage.models import  Productos, Integrantes, Sucursales
from WebPage.forms import FormularioBusqueda, FormularioProducto, FormularioIntegrantes, FormularioSucursales
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from log_web.models import Avatar


# Create your views here.

def inicio(request):
    
     return render(request, "WebPage/index.html")

def productos(request):
       
    lista_productos = Productos.objects.all()

    if request.GET.get("producto"):

        formulario = FormularioBusqueda(request.GET)

        if formulario.is_valid():
           
            data = formulario.cleaned_data
            lista_productos = Productos.objects.filter(nombre__icontains = data["producto"])
        
        return render(request, "WebPage/productos.html", {"productos" : lista_productos, "formulario" : formulario })
    
    else:
        formulario = FormularioBusqueda()
        return render(request, "WebPage/productos.html", {"productos" : lista_productos, "formulario" : formulario})

    

def integrantes(request):
    
    lista_integrantes = Integrantes.objects.all()
    
    return render(request, "WebPage/integrantes.html", {"integrantes" : lista_integrantes})


def sucursales(request):
    
    lista_sucursales = Sucursales.objects.all()
    
    return render(request, "WebPage/sucursales.html", {"sucursales" : lista_sucursales})

@login_required
def productos_carga(request):
    
    if request.method == "GET":
        formulario = FormularioProducto()
        return render (request, "WebPage/form_productos.html", {"formulario":formulario})


    else:

        formulario = FormularioProducto(request.POST, request.FILES)

        if formulario.is_valid(): 

            data = formulario.cleaned_data
           
            nombre = data.get("nombre_producto")
            precio = data.get("precio")
            modelo = data.get("modelo")
            imagen = data["imagen"]
            
            producto = Productos(nombre=nombre, precio=precio, modelo=modelo, imagen=imagen)
        
            producto.save()

            return redirect ("inicio")
        
        else:
            
            return HttpResponse(f"La informacion ingresada no es valida", imagen)

       

def integrantes_carga(request):

    if request.method == "GET":
        formulario = FormularioIntegrantes()
        return render (request, "WebPage/form_integrantes.html", {"formulario":formulario})


    else:

        formulario = FormularioIntegrantes(request.POST)

        if formulario.is_valid(): 

            data = formulario.cleaned_data
           
            nombre = data.get("nombre")
            edad = data.get("edad")
            profesion = data.get("profesion")
            integrante = Integrantes(nombre=nombre, edad=edad, profesion=profesion)
        
            integrante.save()

            return HttpResponse(f"La informacion fue ingresada correctamente")
        
        else:
            
            return HttpResponse(f"La informacion ingresada no es valida")


def sucursales_carga(request):

    if request.method == "GET":
        formulario = FormularioSucursales()
        return render (request, "WebPage/form_sucursales.html", {"formulario":formulario})


    else:

        formulario = FormularioSucursales(request.POST)

        if formulario.is_valid(): 

            data = formulario.cleaned_data
           
            nombre = data.get("nombre_sucursal")
            direccion = data.get("direccion")
            dias = data.get("dias")
            horarios = data.get("horarios")
            sucursal = Sucursales(nombre=nombre, direccion=direccion , dias=dias, horarios=horarios)
        
            sucursal.save()

            return HttpResponse(f"La informacion fue ingresada correctamente")
        
        else:
            
            return HttpResponse(f"La informacion ingresada no es valida")

class lista_productos (ListView):
    model = Productos
    template_name = 'WebPage/leer_prod.html'


class detalle_prod (DetailView):
    model = Productos
    template_name = 'WebPage/detalle_prod.html'


class crear_prod (LoginRequiredMixin, CreateView):
    model = Productos
    success_url = "/WebPage/productos"
    fields = ["nombre", "modelo", "precio"]

class editar_prod (LoginRequiredMixin, UpdateView):
    model = Productos
    success_url = "/WebPage/productos"
    fields = ["nombre", "modelo", "precio", "imagen"]

class borrar_prod (LoginRequiredMixin, DeleteView):
    model = Productos
    success_url = "/WebPage/productos"



def agregar_foto(request):

    if request.method == "GET":
        form = Productos()
        contexto = {"form": form}
        return render(request, "WebPage/productos.html", contexto)
    else:
        form = Productos(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            foto = Productos(imagen=data["imagen"])
            
            print(data)

            foto.save()
            return redirect("inicio")
        contexto = {"form": form, }
        return render(request, "WebPage/productos.html", contexto)


    



