from django.urls import path
from WebPage.views import *

urlpatterns = [
    path('inicio/', index),
    path('integrantes/', integrantes),
    path('sucursales/', sucursales),
    path('productos/carga', productos_carga, name="carga_productos"),
    path('integrantes/carga/', integrantes_carga, name="carga_integrantes"),
    path('sucursales/carga/', sucursales_carga, name ="carga_sucursales"),
]