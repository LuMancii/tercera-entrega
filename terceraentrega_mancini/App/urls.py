from django.urls import path
from App import views
from .views import *

urlpatterns = [
    path('celulares/', celulares, name='Celulares'),
    path('sobre-mi/', sobremi, name='Sobremi'),
    path('', inicio , name = 'Inicio'),
    path('añadircelular/', añadircelular , name = 'AñadirCelular'),
]