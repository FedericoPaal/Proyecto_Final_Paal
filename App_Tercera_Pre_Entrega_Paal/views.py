from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import *
from .carrito_compras import Carrito_Compras
from itertools import chain

# Create your views here.
def inicio(req):
    
    return render(req, "inicio.html")

def crear_Producto(req):       

    if req.method == "POST":
        producto_formulario = Producto_Formulario(req.POST, req.FILES)

        if producto_formulario.is_valid():
            producto_formulario.save()

            img = producto_formulario.instance
            
            return render(req, "inicio.html", {"mi_formulario": producto_formulario, "img": img, "mensaje": "El producto ha sido creado con éxito!"})
    else:
        producto_formulario = Producto_Formulario()
    return render(req, "crearProducto.html", {"mi_formulario": producto_formulario})
    

def eliminar_Producto(req, id):
    if req.method == "POST":

        producto = Producto.objects.get(id=id)
        producto.delete()
        
        if producto.categoria == "NOVEDADES":
            novedades = Producto.objects.all().filter(categoria="NOVEDADES").order_by("id").reverse()
            return render(req, "novedades.html", {"novedades": novedades, "mensaje": "El producto ha sido eliminado con éxito!" })
        
        elif producto.categoria == "LIBROS":
            libros = Producto.objects.all().filter(categoria="LIBROS").order_by("id").reverse()
            return render(req, "libros.html", {"libros": libros, "mensaje": "El producto ha sido eliminado con éxito!"})
        
        elif producto.categoria == "MERCHANDISINGS":
            merchandisings = Producto.objects.all().filter(categoria="MERCHANDISINGS").order_by("id").reverse()
            return render(req, "inicio.html", {"merchandisings": merchandisings, "mensaje": "El producto ha sido eliminado con éxito!"})
    

def editar_Producto(req, id):

    producto = Producto.objects.get(id=id) 

    if req.method == "POST":
        mi_formulario = Producto_Formulario(req.POST, req.FILES, instance=producto)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            producto.titulo = data["titulo"]
            producto.autor = data["autor"]
            producto.precio = data["precio"]
            producto.imagen = data["imagen"]
            producto.creacion = data["creacion"]
            producto.categoria = data["categoria"]
            producto.texto = data["texto"]
            mi_formulario.save()
            
            return render(req, "inicio.html", {"mensaje": "El producto ha sido editado con éxito!"})
    else:
        mi_formulario = Producto_Formulario(initial={
            "titulo": producto.titulo,
            "autor": producto.autor, 
            "precio": producto.precio,
            "imagen": producto.imagen,
            "creacion": producto.creacion,
            "categoria": producto.categoria,
            "texto": producto.texto,
        })
        return render(req, "editarProducto.html", {"mi_formulario": mi_formulario, "id": producto.id})


@login_required
def consulta(req):

    if req.method == "POST":
        consulta_formulario = Consultas_Formulario(req.POST)

        if consulta_formulario.is_valid():
            data = consulta_formulario.cleaned_data
            _consulta = Consulta(nombre=data["nombre"], email=data["email"], consulta=data["consulta"])
            _consulta.save()
            
            return render(req, "inicio.html")
    else:
        consulta_formulario = Consultas_Formulario()
        return render(req, "consulta.html", {"mi_formulario": consulta_formulario})
    
def eliminar_Consulta(req, id):
    if req.method == "POST":
        consulta = Consulta.objects.get(id=id)
        consulta.delete()

        consultas = Consulta.objects.all()
        return render(req, "consulta.html", {"consultas": consultas})
    

def busqueda_objetos(req):
    return render(req, "inicio.html")

def buscar(req: HttpRequest):

    if req.GET["producto"]:
        producto = req.GET["producto"]
        
        productos = Producto.objects.filter(titulo__icontains=producto)

        return render(req, "inicio.html", {"productos": productos})
    
    else:
        return render(req, "inicio.html")


def loginView(req):

    if req.method == "POST":
        
        mi_formulario = AuthenticationForm(req, data=req.POST)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            usuario = data["username"]
            contrasena = data["password"]

            user = authenticate(username=usuario, password=contrasena)
            
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido/a {usuario}!"})
            
        return render(req, "inicio.html", {"mensaje2": f"Usuario y/o contraseña incorrectos. Pruebe de nuevo por favor."})

    else:
        mi_formulario = AuthenticationForm()
        return render(req, "login.html", {"mi_formulario": mi_formulario})
    

def register(req):

    if req.method == "POST":
        
        mi_formulario = UserCreationForm(req.POST)

        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data
            usuario = data["username"]
            mi_formulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        return render(req, "inicio.html", {"mensaje2": f"Repita correctamente la contraseña"})

    else:
        mi_formulario = UserCreationForm()
        return render(req, "registro.html", {"mi_formulario": mi_formulario})
    

def editar_perfil(req):

    usuario = req.user

    if req.method == 'POST':

        mi_formulario = UserEditForm(req.POST, instance=req.user)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "editarUsuario.html", {"mi_formulario": mi_formulario, "mensaje": "El usuario ha sido actualizado con éxito"})
        else:
            return render(req, "editarUsuario.html", {"mi_formulario": mi_formulario})
    
    else:
        mi_formulario = UserEditForm(instance=usuario)
        return render(req, "editarUsuario.html", {"mi_formulario": mi_formulario})


def crea_cliente(req):

    if req.method == "POST":
        
        info = req.POST

        mi_formulario = Cliente_Formulario({
            "nombre": info["nombre"],
            "apellido": info["apellido"],
            "email": info["email"]
        })

        userForm = UserCreationForm({
            "username": info["username"],
            "password1": info["password1"],
            "password2": info["password2"]
        })

        if mi_formulario.is_valid() and userForm.is_valid():
            
            data = mi_formulario.cleaned_data
            data.update(userForm.cleaned_data)

            user =User(username=data["username"])
            user.set_password(data["password1"])
            user.save()

            cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], user=user)
            cliente.save()

            return render(req, "inicio.html", {"mensaje": "Usuario creado con éxito"})

    else:

        mi_formulario = Cliente_Formulario()
        userForm = UserCreationForm()
        return render(req, "clienteFormulario.html", {"mi_formulario": mi_formulario, "userForm": userForm})
    

def about_me(req):
    return render(req, "aboutMe.html")


def carrito_compras(req):

    productos = req.session.get("carrito")

    return render(req, "carrito.html", {"productos": productos})


def lista_consultas(req):

    consultas = Consulta.objects.all()
    return render(req, "consulta.html", {"consultas": consultas})


def libros(req):

    libros = Producto.objects.all().filter(categoria="LIBROS").order_by("id").reverse()
    return render(req, "libros.html", {"libros": libros})


def novedades(req):

    novedades = Producto.objects.all().filter(categoria="NOVEDADES").order_by("id").reverse()
    return render(req, "novedades.html", {"novedades": novedades})


def merchs(req):

    merchs = Producto.objects.all().filter(categoria="MERCHANDISINGS").order_by("id").reverse()
    return render(req, "merchandisings.html", {"merchs": merchs})


def comprar(req):

    carrito = Carrito_Compras(req)
    carrito.limpiar_carrito()
    productos = req.session.get("carrito")
    
    return render(req, "carrito.html", {"mensaje": "La compra de sus producto/s ha sido exitosa! Gracias por elegirnos!", "productos": productos})

@login_required
def agregar_producto(req, producto_id):
    
    carrito = Carrito_Compras(req)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    productos = req.session.get("carrito")

    return render(req, "carrito.html", {"productos": productos})


def eliminar_producto(req, producto_id):
    
    carrito = Carrito_Compras(req)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    productos = req.session.get("carrito")

    return render(req, "carrito.html", {"productos": productos})


def restar_producto(req, producto_id):
    
    carrito = Carrito_Compras(req)  
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    productos = req.session.get("carrito")

    return render(req, "carrito.html", {"productos": productos})


def limpiar_carrito(req):
    
    carrito = Carrito_Compras(req)
    carrito.limpiar_carrito()
    productos = req.session.get("carrito")
    return render(req, "carrito.html", {"productos": productos})


def ver_detalles(req, producto_id):

    producto = Producto.objects.get(id=producto_id)
    if producto.categoria == "LIBROS":
        return render(req, "detallesLibro.html", {"libro": producto})
    
    elif producto.categoria == "NOVEDADES":
        return render(req, "detallesNovedad.html", {"novedad": producto})
    
    elif producto.categoria == "MERCHANDISINGS":
        return render(req, "detallesMerchandising.html", {"merch": producto})


def sin_pagina(req):
    return render(req, "sinPagina.html")