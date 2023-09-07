from django import forms


class Formulario(forms.Form):
    
    nombre = forms.CharField(required= True)
    serie = forms.CharField(required= True)
    precio = forms.DecimalField(required= True)
    memoria = forms.CharField(required= True)
    pantalla = forms.DecimalField(required= True)
    camara = forms.DecimalField(required= True)