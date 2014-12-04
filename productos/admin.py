from django.contrib import admin
from productos.models import LineaProducto, CategoriaProducto, Producto, ImagenProducto

# Register your models here.
admin.site.register(LineaProducto)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(ImagenProducto)


