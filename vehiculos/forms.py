from django import forms 
from vehiculos.models import Autos

class AutosInfo(forms.ModelForm):
    class Meta:
        model = Autos
        fields = ['modelo', 'color', 'marca', 'fecha_de_fabricacion', 'descripcion', 'imagen']

class BusquedaAuto(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)