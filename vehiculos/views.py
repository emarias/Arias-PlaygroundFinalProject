from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
    
class SacarAuto(DeleteView):
    model = Autos
    template_name = "autos/sacar_auto.html"
    success_url= reverse_lazy ('autos')

class EditarAuto(UpdateView):
    model = Autos
    template_name = "autos/editar_auto.html"
    success_url= reverse_lazy ('autos')
    fields= ['modelo', 'color', 'marca', 'fecha_de_fabricacion','descripcion']
    
class DetallesAuto(DetailView):
    model = Autos
    template_name = "autos/detalles_auto.html"
    