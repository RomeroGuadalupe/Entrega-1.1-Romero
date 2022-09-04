from datetime import datetime
from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class Mensajes(models.Model):
    texto = models.CharField(max_length=500)
    emisor = models.CharField(max_length=150)
    fecha = models.DateField(db_column= 'fecha', blank= True, null = True)
    receptor = models.CharField(max_length=150)

    
    def __str__(self):
        return f"{self.texto} - {self.emisor} - {self.fecha} "
