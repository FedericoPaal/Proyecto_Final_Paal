from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import *
from .forms import *

# Create your views here.
def inicio(req):
    return render(req, "inicio.html")


def novedad(req):

    if req.method == "POST":
        novedad_formulario = Novedades_Formulario(req.POST)

        if novedad_formulario.is_valid():
            data = novedad_formulario.cleaned_data
            _novedad = Novedad(titulo=data["titulo"], autor=data["autor"], precio=data["precio"])
            _novedad.save()

            return render(req, "inicio.html")
    else:
        novedad_formulario = Novedades_Formulario()
        return render(req, "novedad.html", {"mi_formulario": novedad_formulario})


def libro(req):

    if req.method == "POST":
        libro_formulario = Libros_Formulario(req.POST)

        if libro_formulario.is_valid():
            data = libro_formulario.cleaned_data
            _libro = Libro(titulo=data["titulo"], autor=data["autor"], precio=data["precio"])
            _libro.save()
            
            return render(req, "inicio.html")
    else:
        libro_formulario = Libros_Formulario()
        return render(req, "libro.html", {"mi_formulario": libro_formulario})


def merchandising(req):

    if req.method == "POST":
        merchandising_formulario = Merchandising_Formulario(req.POST)

        if merchandising_formulario.is_valid():
            data = merchandising_formulario.cleaned_data
            _merchandising = Merchandising(nombre=data["nombre"], precio=data["precio"])
            _merchandising.save()
            
            return render(req, "inicio.html")
    else:
        merchandising_formulario = Merchandising_Formulario()
        return render(req, "merchandising.html", {"mi_formulario": merchandising_formulario})
    

def consulta(req):

    if req.method == "POST":
        consulta_formulario = Consultas_Formulario(req.POST)

        if consulta_formulario.is_valid():
            data = consulta_formulario.cleaned_data
            _consulta = Consulta(nombre=data["nombre"], email=data["email"], precio=data["precio"])
            _consulta.save()
            
            return render(req, "inicio.html")
    else:
        consulta_formulario = Consultas_Formulario()
        return render(req, "consulta.html", {"mi_formulario": consulta_formulario})
    

def busqueda_objetos(req):
    return render(req, "inicio.html")

def buscar(req: HttpRequest):

    if req.GET["producto"]:
        producto = req.GET["producto"]
        
        productos = Libro.objects.filter(titulo__icontains=producto)

        return render(req, "inicio.html", {"productos": productos})
    else:
        return HttpResponse(f"No se encontro en la busqueda")

