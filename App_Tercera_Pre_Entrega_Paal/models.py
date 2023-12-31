from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True, upload_to='Productos')
    creacion = models.DateField(null=True, blank=True)
    categoria = models.CharField(max_length=40)
    texto = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}"
    

class Novedad(models.Model):

    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True, upload_to='Novedades')
    creacion = models.DateField(null=True, blank=True)
    texto = models.CharField(max_length=500, null=True, blank=True)

    class Meta():

        verbose_name_plural = "Novedades"

    def __str__(self):
        return f"{self.titulo}"


class Libro(models.Model):

    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True, upload_to='Libros')
    creacion = models.DateField(null=True, blank=True)
    texto = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}"


class Merchandising(models.Model):

    titulo = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True, upload_to='Merchandising')
    creacion = models.DateField(null=True, blank=True)
    texto = models.CharField(max_length=500, null=True, blank=True)

    class Meta():
        verbose_name_plural = "Merchandising"

    def __str__(self):
        return f"{self.titulo}"


class Consulta(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    consulta = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.consulta}"
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Staff(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
