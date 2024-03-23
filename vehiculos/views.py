from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from vehiculos.models import Autos
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from vehiculos.forms import BusquedaAuto, AutosInfo

class AutosLista(ListView):
    model = Autos
    context_object_name = 'autos'
    template_name = "autos/autos.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        formulario = BusquedaAuto(self.request.GET)
        
        if formulario.is_valid():
            texto_busqueda = formulario.cleaned_data.get("nombre")
            if texto_busqueda:
                queryset = queryset.filter(marca__icontains=texto_busqueda)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = BusquedaAuto(self.request.GET)
        return context

    
class PedirAuto(LoginRequiredMixin,CreateView):
    model = Autos
    template_name = "autos/conseguir_auto.html"
    form_class = AutosInfo
    success_url = reverse_lazy('autos')
    
class SacarAuto(LoginRequiredMixin, DeleteView):
    model = Autos
    template_name = "autos/sacar_auto.html"
    success_url= reverse_lazy ('autos')

class EditarAuto(LoginRequiredMixin,UpdateView):
    model = Autos
    template_name = "autos/editar_auto.html"
    form_class = AutosInfo
    success_url = reverse_lazy('autos')
    
class DetallesAuto(DetailView):
    model = Autos
    template_name = "autos/detalles_auto.html"
    