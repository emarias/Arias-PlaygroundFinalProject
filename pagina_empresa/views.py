from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from pagina_empresa.models import Empleado
from pagina_empresa.forms import FormularioNuevoEmpleado, BusquedaEmpleado, FormularioEditarEmpleado

def inicio(request):
    return render(request,'pagina_empresa/inicio.html')
    #return render(request,'base.html')

def crear_empleado(request):
    formulario = FormularioNuevoEmpleado()
    if request.method == "POST":
        formulario = FormularioNuevoEmpleado(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get("nombre")
            apellido = formulario.cleaned_data.get("apellido")
            edad = formulario.cleaned_data.get("edad")
            sector = formulario.cleaned_data.get("sector")
            sobre_mi = formulario.cleaned_data.get("sobre_mi")
            empleado = Empleado(nombre=nombre, apellido=apellido, edad=edad, sector=sector, sobre_mi=sobre_mi)
            empleado.save()
            return redirect("empleados")
    return render(request, "pagina_empresa/crear_empleado.html", {'formulario':formulario})

def empleados(request):
    
    formulario = BusquedaEmpleado(request.GET)
    if formulario.is_valid():
        busqueda = formulario.cleaned_data.get("nombre")
        empleadoslista = Empleado.objects.filter(nombre__icontains=busqueda)
        
    return render(request,'pagina_empresa/empleados.html', {'empleadoslista':empleadoslista, 'formulario':formulario})

def eliminar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    empleado.delete()
    return redirect("empleados")
    
def editar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    formulario = FormularioEditarEmpleado(initial= {'nombre':empleado.nombre, 'apellido': empleado.apellido, 'edad': empleado.edad, 'sector': empleado.sector, 'sobre_mi':empleado.sobre_mi })
    
    if request.method == "POST":
        formulario = FormularioEditarEmpleado(request.POST)
        if formulario.is_valid():
            nueva_info= formulario.cleaned_data
            
            empleado.nombre = nueva_info.get("nombre")
            empleado.apellido = nueva_info.get("apellido")
            empleado.edad = nueva_info.get("edad")
            empleado.sector = nueva_info.get("sector")
            empleado.sobre_mi = nueva_info.get("sobre_mi")
            
            empleado.save()
            return redirect('empleados')
    
    return render(request, 'pagina_empresa/editar_empleado.html',{"empleado":empleado,"formulario":formulario})
    
def ver_empleado(request,id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    return render(request, 'pagina_empresa/ver_empleado.html', {'empleado':empleado})