from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('novedad/', novedad, name="Novedades"),
    path('libro/', libro, name="Libros"),
    path('merchandising/', merchandising, name="Merchandising"),
    path('consulta/', consulta, name="Consultas"),

]