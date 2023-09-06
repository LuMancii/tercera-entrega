from django.shortcuts import render
from django.http import HttpResponse

def inicio(req):
    
    return render(req, 'inicio.html')

def celulares(req):
    return render(req, 'celulares.html')

def sobremi(req):
    return render(req, 'sobremi.html')

def añadircelular(request):
    
    return render(request, 'añadircelular.html')
