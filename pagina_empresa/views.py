from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from pagina_empresa.models import Empleado
from pagina_empresa.forms import FormularioNuevoEmpleado

def inicio(request):
    return render(request,'inicio.html')

def crear_empleado(request):
    formulario = FormularioNuevoEmpleado()
    if request.method == "POST":
        formulario = FormularioNuevoEmpleado(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get("nombre")
            apellido = formulario.cleaned_data.get("apellido")
            edad = formulario.cleaned_data.get("edad")
            sector = formulario.cleaned_data.get("sector")
            empleado = Empleado(nombre=nombre, apellido=apellido, edad=edad, sector=sector)
            empleado.save()
            return redirect("empleados")
    return render(request, "crear_empleado.html", {'formulario':formulario})

def empleados(request):
    empleadoslista = Empleado.objects.all()
    return render(request,'empleados.html', {'empleadoslista':empleadoslista})