from django.urls import path
from App import views
from .views import *

urlpatterns = [
    path('celulares/', celulares, name='Celulares'),
    path('sobre-mi/', sobremi, name='Sobremi'),
    path('anadircelular/', anadircelular , name = 'Anadir'),
    path('', inicio , name = 'Inicio'),
    path('busqueda-celular/', busqueda_celular , name = 'BusquedaCelular'),
    path('buscar/', buscar , name = 'Buscar'),
]