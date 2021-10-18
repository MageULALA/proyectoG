from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class Cliente (models.Model):
        idCliente = models.AutoField(primary_key=True)
        nombre= models.CharField(max_length=100)
        direccion = models.CharField(max_length=200)
        telefono = models.CharField(max_length=9)

class TipoProducto(models.Model):
        idTipoProducto = models.AutoField(primary_key=True)
        nombreTipoPro = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=100)
        def __str__(self):
            return self.nombreTipoPro


class Producto(models.Model):
        idProducto = models.AutoField(primary_key=True)
        nombrePro = models.CharField(max_length=50)
        tipoProducto = models.ForeignKey('TipoProducto', on_delete= models.DO_NOTHING, default=1)
        precioU = models.DecimalField(decimal_places=2, max_digits=10)
        def __str__(self):
            return self.nombrePro

