from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User 
import uuid

# Create your models here.

class Modelo_Usuario(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, editable=False)
    tiempo = models.DateTimeField(auto_now_add=True)
    actualizar = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

# Para que se borre todo una vez que se borre el canal
class Canal_Mensaje(models.Model):
    canal = models.ForeignKey("Canal", on_delete=CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()

# Para que el usuario pueda acceder a sus mensajes aunque se borre su canal
class Canal_Usuario(Modelo_Usuario): 
    canal = models.ForeignKey("Canal", null=True, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


# Para que se comuniquen muchos usuarios entre si
class Canal(Modelo_Usuario):
    usuarios = models.ManyToManyField(User, blank=True, through=Canal_Usuario)