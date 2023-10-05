from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),

    #Consultas
    path('consulta/', consulta, name="Consultas"),
    path('_consultas/', lista_consultas, name="Lista_Consultas"),
    path('eliminar-consulta/<int:id>', eliminar_Consulta, name="Eliminar_Consultas"),

    #Busqueda
    path('busqueda-objetos/', busqueda_objetos, name="Busqueda_Objetos"),
    path('buscar/', buscar, name="Buscar"),

    #Login & Register
    path('login/', loginView, name="Login"),
    path('register/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar-usuario/', editar_perfil, name="Editar_Usuario"),
    path('register-cliente/', crea_cliente, name="Crea_Cliente"),

    #Footer 
    path('about-me/', about_me, name="About_Me"),
    path('sin-pagina/', sin_pagina, name="Sin_Pagina"),

    #Detalles Productos
    path('detalles-productos/<int:producto_id>/', ver_detalles, name="Detalles_Productos"),


    #Agregar Productos
    path('crear-producto/', crear_Producto, name="Crear_Productos"),


    #Eliminar Productos
    path('eliminar-producto/<int:id>', eliminar_Producto, name="Eliminar_Productos"),
    

    #Editar Productos
    path('editar-producto/<int:id>', editar_Producto, name="Editar_Productos"),
    

    #Listas Productos
    path('_libros/', libros, name="_Libros"),
    path('_merchs/', merchs, name="_Merchs"),
    path('_novedades/', novedades, name="_Novedades"),

    #Funciones Carrito
    path('carrito-compras/', carrito_compras, name="Carrito_de_Compras"),
    path('comprar/', comprar, name="Comprar"),
    
    #Productos
    path('agregar/<int:producto_id>/', agregar_producto, name="Agregar_"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Eliminar_"),
    path('restar/<int:producto_id>/', restar_producto, name="Restar_"),

    path('limpiar/', limpiar_carrito, name="Limpiar_"),

]

