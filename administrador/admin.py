from django.contrib import admin
from administrador.models import Servicio, Tarjeta, Perfil, Anuncio, Paquete, Venta, Licencia
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    #lo que muestra
    list_display=("id","nombre","vigencia")
    #porque cambios puedes buscar
    search_fields=("id","nombre")
    #como filtramos esta clase
    list_filter=("vigencia",)
    #ordenar
    ordering = ("-nombre",)
    #editar campos en vista
    list_editable = ("nombre",)

class PaqueteAdmin(admin.ModelAdmin):
    list_display=("id","descripcion","cantidadAnuncios","duracionDias","precio")
    search_fields=("paquete_id","descripcion")
    list_filter=("duracionDias","precio","cantidadAnuncios","vigencia",)
    list_editable = ("precio",)


class VentaAdmin(admin.ModelAdmin):
    list_display=("id","total","tarjeta_id")
    search_fields=("id","tarjeta_id","fecha")
    list_filter=("fecha",)

class LicenciaAdmin(admin.ModelAdmin):
    list_display=("id","paquete_id","venta_id","estado", "precio")
    search_fields=("idLicencia","idPaquete","idVenta")
    list_filter=("estado","fecha_inicio","fecha_fin",)

class TarjetaAdmin(admin.ModelAdmin):
    list_display=("id","nombreTarjeta","numeroTarjeta","user_id")
    search_fields=("id","nombreTarjeta")

class AnuncioAdmin(admin.ModelAdmin):
    list_display=("id","titulo","departamento_id","servicio_id","user_id","licencia_id" )
    search_fields=("id","titulo","departamento_id","servicio_id","usuario_id")
    list_filter=("departamento_id","estado",)


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Tarjeta, TarjetaAdmin)
admin.site.register(Perfil)
admin.site.register(Anuncio, AnuncioAdmin)
#admin.site.register(Seguidor)
#admin.site.register(Favorito)
admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Licencia, LicenciaAdmin)

