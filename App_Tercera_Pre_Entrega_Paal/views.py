from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def novedad(req):
    return HttpResponse(f"Vista de Novedades")


def libro(req):
    return HttpResponse(f"Vista de Libros")


def merchandising(req):
    return HttpResponse(f"Vista de Merchandising")


def consulta(req):
    return HttpResponse(f"Vista de Consulta")