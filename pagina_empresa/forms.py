from django import forms 
from ckeditor.fields import RichTextFormField
from pagina_empresa.models import Empleado

class FormularioBaseEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    sector = forms.CharField(max_length=30)
    sobre_mi = RichTextFormField()
    imagen = forms.ImageField(required=False) 

class FormularioNuevoEmpleado(FormularioBaseEmpleado):
    ...


class FormularioEditarEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'edad', 'sector', 'sobre_mi', 'imagen']
    
class BusquedaEmpleado(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)