from django.contrib import admin
from administrador.models import Anuncio,Favorito,Foto,Licencia,Paquete,Seguidor,Servicio,Tarjeta,Usuario,Venta
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    #lo que muestra
    list_display=("idServicio","descripcion","vigencia")
    #porque cambios puedes buscar
    search_fields=("idServicio","descripcion")
    #como filtramos esta clase
    list_filter=("vigencia",)
    #ordenar
    ordering = ("-descripcion",)
    #editar campos en vista
    list_editable = ("descripcion",)

class FotoAdmin(admin.ModelAdmin):
    list_display=("idFoto","ruta")
    search_fields=("idFoto","ruta")

class TarjetaAdmin(admin.ModelAdmin):
    list_display=("idTarjeta","nombreTarjeta","numeroTarjeta","idUsuario")
    search_fields=("idTarjeta","nombreTarjeta")

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("idUsuario","nombres","cuenta")
    search_fields=("idUsuario","nombres","cuenta","telefono")

class AnuncioAdmin(admin.ModelAdmin):
    list_display=("idAnuncio","titulo","departamento","idServicio","idUsuario","idLicencia" )
    search_fields=("idAnuncio","titulo","idServicio","idUsuario")
    list_filter=("departamento","vigencia","permitido",)

class SeguidorAdmin(admin.ModelAdmin):
    list_display=("id","idUsuario","idUsuarioSeguidor")
    search_fields=("id","idUsuario","idUsuarioSeguidor")

class FavoritoAdmin(admin.ModelAdmin):
    list_display=("id","idUsuario","idAnuncio","fecha_guardado")
    search_fields=("id","idUsuario","idAnuncio")
    list_filter=("fecha_guardado",)

class PaqueteAdmin(admin.ModelAdmin):
    list_display=("idPaquete","descripcion","cantidadAnuncios","duracionDias","precio")
    search_fields=("idPaquete","descripcion")
    list_filter=("duracionDias","precio","cantidadAnuncios","vigencia",)
    list_editable = ("precio",)

class VentaAdmin(admin.ModelAdmin):
    list_display=("idVenta","descuento","total","idTarjeta")
    search_fields=("idVenta","idTarjeta","fecha")
    list_filter=("descuento","fecha","hora",)

class LicenciaAdmin(admin.ModelAdmin):
    list_display=("idLicencia","idPaquete","idVenta","estado")
    search_fields=("idLicencia","idPaquete","idVenta")
    list_filter=("estado","fecha_inicio","fecha_fin",)

admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Foto,FotoAdmin)
admin.site.register(Tarjeta,TarjetaAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Anuncio,AnuncioAdmin)
admin.site.register(Seguidor,SeguidorAdmin)
admin.site.register(Favorito,FavoritoAdmin)
admin.site.register(Paquete,PaqueteAdmin)
admin.site.register(Venta,VentaAdmin)
admin.site.register(Licencia,LicenciaAdmin)

