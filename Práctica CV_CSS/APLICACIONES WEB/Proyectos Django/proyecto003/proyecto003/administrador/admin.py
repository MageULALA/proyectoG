from django.contrib import admin
from administrador.models import Cliente, Producto, TipoProducto
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("idCliente","nombre","telefono")
    search_fields= ("nombre","telefono")


class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ("nombreTipoPro","descripcion")

class ProductoAdmin(admin.ModelAdmin):
    list_display= ("nombrePro","tipoProducto")
    search_fields= ("nombrePro",)
    list_filter = ("nombrePro","precioU")

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(TipoProducto,TipoProductoAdmin)
admin.site.register(Producto,ProductoAdmin)

