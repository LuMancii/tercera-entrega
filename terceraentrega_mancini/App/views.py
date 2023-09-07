from django.shortcuts import render
from django.http import HttpResponse
from .models import Celular
from .forms import *


def inicio(req):
    
    return render(req, 'inicio.html')

def celulares(req):
    return render(req, 'celulares.html')

def sobremi(req):
    return render(req, 'sobremi.html')

def anadircelular(request):
    
    if request.method == 'POST':
        
        miFormulario = Formulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
      
            celular =  Celular(nombre = informacion['nombre'], 
                               serie = informacion['serie'], 
                               precio = informacion['precio'], 
                               memoria = informacion['memoria'], 
                               pantalla = informacion['pantalla'], 
                               camara = informacion['camara'] )
 
            celular.save()
 
            return render(request, "inicio.html")
        
    else:
            miFormulario = Formulario()
 
    return render(request,"anadircelular.html", {'miFormulario': miFormulario})

def busqueda_celular(req):
    
    return render(req, 'busquedacelular.html')

def buscar(req):
    
    if req.GET['nombre']:
        nombre = req.GET['nombre']
        series = Celular.objects.filter(nombre=nombre)
        if series:
            return render(req,"resultadoBusqueda.html", {'serie': series})
    else:
        return HttpResponse('no se escribio ningun nombre de celular')
        
