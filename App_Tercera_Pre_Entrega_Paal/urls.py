from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('novedad/', novedad, name="Novedades"),
    path('libro/', libro, name="Libros"),
    path('merchandising/', merchandising, name="Merchandising"),
    path('consulta/', consulta, name="Consultas"),
    path('busqueda-objetos/', busqueda_objetos, name="Busqueda_Objetos"),
    path('buscar/', buscar, name="Buscar"),
    path('login/', loginView, name="Login"),
    path('register/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
]