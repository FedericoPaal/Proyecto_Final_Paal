from django.db import models

# Create your models here.

class Novedad(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=40)


class Libro(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=40)


class Merchandising(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=40)


class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)