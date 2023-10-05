from django.contrib import admin
from .models import Novedad, Libro, Merchandising, Consulta, Staff, Cliente, Producto

# Register your models here.
admin.site.register(Novedad)
admin.site.register(Libro)
admin.site.register(Merchandising)
admin.site.register(Consulta)
admin.site.register(Staff)
admin.site.register(Cliente)
admin.site.register(Producto)