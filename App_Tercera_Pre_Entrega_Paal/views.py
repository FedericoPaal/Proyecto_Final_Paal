from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def inicio(req):
    return render(req, "inicio.html")


def novedad(req):
    return render(req, "novedad.html")


def libro(req):
    return render(req, "libro.html")


def merchandising(req):
    return render(req, "merchandising.html")


def consulta(req):
    return render(req, "consulta.html")