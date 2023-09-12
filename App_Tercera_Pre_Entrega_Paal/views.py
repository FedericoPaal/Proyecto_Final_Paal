from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import *
from .forms import *

# Create your views here.
def inicio(req):
    return render(req, "inicio.html")


def novedad(req):

    if req.method == "POST":
        mi_formulario = Novedades_Formulario(req.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            _novedad = Novedad(titulo=data["titulo"], autor=data["autor"], precio=data["precio"])
            _novedad.save()

            return render(req, "inicio.html")
    else:
        mi_formulario = Novedades_Formulario()
        return render(req, "novedad.html", {"mi_formulario": mi_formulario})


def libro(req):

    if req.method == "POST":
        mi_formulario = Libros_Formulario(req.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            _novedad = Novedad(titulo=data["titulo"], autor=data["autor"], precio=data["precio"])
            _novedad.save()
            
            return render(req, "inicio.html")
    else:
        mi_formulario = Libros_Formulario()
        return render(req, "libro.html", {"mi_formulario": mi_formulario})


def merchandising(req):

    if req.method == "POST":
        mi_formulario = Merchandising_Formulario(req.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            _novedad = Novedad(nombre=data["nombre"], precio=data["precio"])
            _novedad.save()
            
            return render(req, "inicio.html")
    else:
        mi_formulario = Merchandising_Formulario()
        return render(req, "merchandising.html", {"mi_formulario": mi_formulario})
    

def consulta(req):

    if req.method == "POST":
        mi_formulario = Consultas_Formulario(req.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            _novedad = Novedad(nombre=data["nombre"], email=data["email"], precio=data["precio"])
            _novedad.save()
            
            return render(req, "inicio.html")
    else:
        mi_formulario = Consultas_Formulario()
        return render(req, "consulta.html", {"mi_formulario": mi_formulario})
    

def busqueda_objetos(req):
    return render(req, "inicio.html")

def buscar(req: HttpRequest):

    if req.GET["producto"]:
        producto = req.GET["producto"]
        
        objetos = Novedad.objects.filter(titulo__icontains=producto), Libro.objects.filter(titulo__icontains=producto), Merchandising.objects.filter(nombre__icontains=producto)

        productos = objetos

        return render(req, "inicio.html", {"productos": productos})
    else:
        return HttpResponse(f"No se encontro en la busqueda")

