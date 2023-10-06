from django.contrib import admin
from .models import Consulta, Staff, Cliente, Producto

# Register your models here.
admin.site.register(Consulta)
admin.site.register(Staff)
admin.site.register(Cliente)
admin.site.register(Producto)