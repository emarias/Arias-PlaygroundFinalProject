from django import forms 

class BusquedaAuto(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)