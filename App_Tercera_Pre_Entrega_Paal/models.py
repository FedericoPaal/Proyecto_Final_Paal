from django.db import models

# Create your models here.

class Novedad(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.CharField(max_length=40)

    class Meta():

        verbose_name_plural = "Novedades"

    def __str__(self):
        return f"{self.titulo}"

class Libro(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.titulo}"

class Merchandising(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.CharField(max_length=40)

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

class Consultas_Usuarios(models.Model):

    consulta_usuario = models.ForeignKey(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.consulta_usuario.nombre}"