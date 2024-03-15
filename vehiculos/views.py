from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from vehiculos.models import Autos
from django.urls import reverse_lazy

class AutosLista(ListView):
    model = Autos
    context_object_name = 'autos'
    template_name = "autos/autos.html"

    
class PedirAuto(CreateView):
    model = Autos
    template_name = "autos/conseguir_auto.html"
    fields = ['modelo', 'color', 'marca', 'fecha_de_fabricacion','descripcion']
    success_url = reverse_lazy('autos')