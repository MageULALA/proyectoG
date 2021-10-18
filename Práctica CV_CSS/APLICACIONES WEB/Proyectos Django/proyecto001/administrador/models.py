from django.db import models

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)

class Seccion(models.Model):
    idseccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

class Articulo(models.Model):
    idArticulo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    seccion = models.ForeignKey('Seccion',on_delete=models.DO_NOTHING, default=1)
    precio = models.DecimalField(decimal_places=2,max_digits=12)

