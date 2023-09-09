from django.http import HttpResponse
from django.template import Template, Context, loader

def inicio(req):
    return HttpResponse(f"Vista de Inicio")