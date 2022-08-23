from django.urls import path
from WebPage.views import *

urlpatterns = [
    path('inicio/', index, name="inicio"),
    path('integrantes/', integrantes, name="integrantes"),
    path('sucursales/', sucursales, name="sucursales"),
    path('productos/carga', productos_carga, name="carga_productos"),
    path('integrantes/carga/', integrantes_carga, name="carga_integrantes"),
    path('sucursales/carga/', sucursales_carga, name ="carga_sucursales"),
]