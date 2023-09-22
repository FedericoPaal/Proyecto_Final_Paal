from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import *

# Create your views here.
def inicio(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url_avatar": avatar.imagen.url})
    except:
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
    
def libros(req):
    lista_libros = Libro.objects.all()

    return render(req, "listaLibros.html", {"lista_libros": lista_libros})

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
    

def busqueda_objetos(req):
    return render(req, "inicio.html")

def buscar(req: HttpRequest):

    if req.GET["producto"]:
        producto = req.GET["producto"]
        
        productos = Libro.objects.filter(titulo__icontains=producto)

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


def agregar_avatar(req):

    if req.method == 'POST':

        mi_formulario = Avatar_Formulario(req.POST, req.FILES)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            avatar.save()

            return render(req, "agregarAvatar.html", {"mensaje": "El avatar ha sido actualizado con éxito"})
    
    else:
        mi_formulario = Avatar_Formulario()
        return render(req, "agregarAvatar.html", {"mi_formulario": mi_formulario})


def carrito_compras(req: HttpRequest):

    productos_carrito = Libro.objects.all()

    lista_carrito = productos_carrito

    return render(req, "carrito.html", {"lista_carrito": lista_carrito})


def comprar(req):
    return render(req, "carrito.html", {"mensaje": "La compra de sus producto/s ha sido exitosa! Gracias por elegirnos!"})


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


def agregar_al_carrito(req):

    acumulador_productos = []

    productos_carrito = Libro.objects.all()

    lista_carrito = productos_carrito

    acumulador_productos += lista_carrito

    return render(req, "carrito.html", {"acumulador_productos": acumulador_productos})