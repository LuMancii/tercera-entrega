from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Celular(models.Model):
    #series = [('serie A', 'Serie A')
              #('serie S', 'Serie S')
              #('serie Z', 'Serie Z')
              #('serie M', 'Serie M')
              #]
    nombre = models.CharField(max_length=40)
    serie = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits= 8, decimal_places=2)
    memoria = models.CharField(max_length=20)
    pantalla = models.DecimalField(max_digits=2, decimal_places=1)
    camara = models.DecimalField(max_digits=3, decimal_places=1)
    descripcion = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    
    
    
class Post(models.Model):
    
    Post =models.ForeignKey(User, on_delete=models.CASCADE, related_name='Post')
    #aca tmb faltan mas parametros
    
