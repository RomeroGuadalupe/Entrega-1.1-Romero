from django.forms import Form, CharField, DateField
from email.policy import default
from datetime import datetime


class FormularioMensajes(Form):
    texto_mensaje = CharField(max_length=500)
    emisor_mensaje = CharField(max_length=150)
    fecha = datetime.today()
    receptor_mensaje = CharField(max_length=150)
   
    
