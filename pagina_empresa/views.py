from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from pagina_empresa.models import Empleado
from pagina_empresa.forms import FormularioNuevoEmpleado, BusquedaEmpleado, FormularioEditarEmpleado
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request,'pagina_empresa/inicio.html')

@login_required
def crear_empleado(request):
    formulario = FormularioNuevoEmpleado()
    if request.method == "POST":
        print(request.POST)  
        print(request.FILES)  
        formulario = FormularioNuevoEmpleado(request.POST, request.FILES)
        if formulario.is_valid():
            print(formulario.cleaned_data)  
            nombre = formulario.cleaned_data.get("nombre")
            apellido = formulario.cleaned_data.get("apellido")
            edad = formulario.cleaned_data.get("edad")
            sector = formulario.cleaned_data.get("sector")
            sobre_mi = formulario.cleaned_data.get("sobre_mi")
            imagen = request.FILES.get("imagen")  
            print(imagen) 
            
            empleado = Empleado(nombre=nombre, apellido=apellido, edad=edad, sector=sector, sobre_mi=sobre_mi, imagen=imagen)
            empleado.save()
            return redirect("empleados")
    return render(request, "pagina_empresa/crear_empleado.html", {'formulario': formulario})



def empleados(request):
    
    formulario = BusquedaEmpleado(request.GET)
    if formulario.is_valid():
        busqueda = formulario.cleaned_data.get("nombre")
        empleadoslista = Empleado.objects.filter(nombre__icontains=busqueda)
        
    return render(request,'pagina_empresa/empleados.html', {'empleadoslista':empleadoslista, 'formulario':formulario})

@login_required
def eliminar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    empleado.delete()
    return redirect("empleados")
    

@login_required
def editar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    formulario = FormularioEditarEmpleado(instance=empleado)
    if request.method == "POST":
        formulario = FormularioEditarEmpleado(request.POST, request.FILES, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleados')
    return render(request, 'pagina_empresa/editar_empleado.html', {"empleado": empleado, "formulario": formulario})
    
def ver_empleado(request,id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    return render(request, 'pagina_empresa/ver_empleado.html', {'empleado':empleado})

def about(request):
    return render(request, 'pagina_empresa/acercaDeMi.html', {})