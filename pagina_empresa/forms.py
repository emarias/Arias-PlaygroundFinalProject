from django import forms 

class FormularioNuevoEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    sector = forms.CharField(max_length=30)
    
class BusquedaEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)