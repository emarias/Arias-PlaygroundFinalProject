from django import forms 

class FormularioBaseEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    sector = forms.CharField(max_length=30)
    
class FormularioNuevoEmpleado(FormularioBaseEmpleado):
    ...


class FormularioEditarEmpleado(FormularioBaseEmpleado):
    ...
    
class BusquedaEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)