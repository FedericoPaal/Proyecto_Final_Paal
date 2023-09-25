from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Novedad(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.CharField(max_length=40)
    imagen = models.ImageField(null=True, blank=True, upload_to='Novedades')

    class Meta():

        verbose_name_plural = "Novedades"

    def __str__(self):
        return f"{self.titulo}"

class Libro(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.CharField(max_length=40)
    imagen = models.ImageField(null=True, blank=True, upload_to='Libros')

    def __str__(self):
        return f"{self.titulo}"

class Merchandising(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.CharField(max_length=40)
    imagen = models.ImageField(null=True, blank=True, upload_to='Merchandising')

    class Meta():
        verbose_name_plural = "Merchandising"

    def __str__(self):
        return f"{self.nombre}"


class Consulta(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    consulta = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.consulta}"

class Consultas_Clientes(models.Model):

    consulta_cliente = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.consulta_cliente.nombre}"
    

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return f"{self.imagen}"
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
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