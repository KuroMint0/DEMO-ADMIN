from django.contrib import admin
from shop.models import producto

# Register your models here.

class productoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'stock', 'precio', 'fecha_salida', 'categoria']

admin.site.register(producto, productoAdmin)