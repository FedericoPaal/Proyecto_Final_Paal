from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),

    path('consulta/', consulta, name="Consultas"),
    path('busqueda-objetos/', busqueda_objetos, name="Busqueda_Objetos"),
    path('buscar/', buscar, name="Buscar"),
    path('login/', loginView, name="Login"),
    path('register/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar-usuario/', editar_perfil, name="Editar_Usuario"),
    path('agregar-avatar/', agregar_avatar, name="Agregar_Avatar"),  #NO SE USA
    path('carrito-compras/', carrito_compras, name="Carrito_de_Compras"),
    path('comprar/', comprar, name="Comprar"),
    path('register-cliente/', crea_cliente, name="Crea_Cliente"),
    path('about-me/', about_me, name="About_Me"),

    #Agregar Productos
    path('agregar-novedad/', agregar_Novedad, name="Agregar_Novedades"),
    path('agregar-libro/', agregar_Libro, name="Agregar_Libros"),
    path('agregar-merchandising/', agregar_Merchandising, name="Agregar_Merchandisings"),

    #Eliminar Productos
    path('eliminar-novedad/<int:id>', eliminar_Novedad, name="Eliminar_Novedades"),
    path('eliminar-libro/<int:id>', eliminar_Libro, name="Eliminar_Libros"),
    path('eliminar-merchandising/<int:id>', eliminar_Merchandising, name="Eliminar_Merchandisings"),

    #Editar Productos
    path('editar-novedad/<int:id>', editar_Novedad, name="Editar_Novedades"),
    path('editar-libro/<int:id>', editar_Libro, name="Editar_Libros"),
    path('editar-merchandising/<int:id>', editar_Merchandising, name="Editar_Merchandisings"),

    #Listas Productos
    path('_libros/', libros, name="_Libros"),
    path('_merchs/', merchs, name="_Merchs"),
    path('_novedades/', novedades, name="_Novedades"),

    #Funciones Carrito
    path('agregar/<int:producto_id>/', agregar_producto, name="Agregar_"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Eliminar_"),
    path('restar/<int:producto_id>/', restar_producto, name="Restar_"),
    path('limpiar/', limpiar_carrito, name="Limpiar_"),

]

