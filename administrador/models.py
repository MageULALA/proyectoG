from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rutaimagen = models.ImageField(upload_to="usuarios", default="usuarios/fotonn.png", null=True, blank=True)
    auth_token = models.CharField(null=True, blank=True,max_length=100)
    confirmada = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    descripcion = models.CharField(max_length=80)
    cantidadAnuncios = models.SmallIntegerField(default=1)
    duracionDias = models.SmallIntegerField(default=6)
    precio = models.DecimalField(decimal_places=2,max_digits=6)
    vigencia = models.CharField(max_length=1,default="V", blank=True)
    def __str__(self):
        return self.descripcion

class Tarjeta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarjetasUsuario')
    nombreTarjeta=models.CharField(max_length=30)
    numeroTarjeta=models.CharField(max_length=16)
    fechaExpiracion=models.DateField()
    cvc=models.CharField(max_length=4)
    def __str__(self):
        return self.nombreTarjeta

class Venta(models.Model):
    tarjeta=models.ForeignKey('Tarjeta',on_delete=models.DO_NOTHING, related_name='ventasTarjeta')
    fecha= models.DateTimeField(default=timezone.now)
    total = models.DecimalField(decimal_places=2,max_digits=8) 

class Licencia(models.Model):
    paquete = models.ForeignKey('Paquete',on_delete=models.DO_NOTHING, related_name='licenciasPaquete')
    venta = models.ForeignKey('Venta',on_delete=models.DO_NOTHING, related_name='licenciasVenta')
    fecha_inicio=models.DateField(null=True)
    fecha_fin=models.DateField(null=True)
    precio = models.DecimalField(decimal_places=2,max_digits=6, null=True, blank=True)
    estado = models.CharField(max_length=1,default="A",null=True, blank=True) #activo, programado, expirado

    def __str__(self):
        return self.descripcion

class Servicio(models.Model):
    nombre=models.CharField(max_length=80)
    vigencia = models.CharField(max_length=1,default="V", blank=True)
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['-nombre']

class Anuncio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anunciosUsuario')
    servicio = models.ForeignKey('Servicio',on_delete=models.DO_NOTHING, related_name='anunciosServicio')
    departamento = models.ForeignKey('Departamento', on_delete=models.DO_NOTHING, related_name='anunciosDepartamento')
    licencia =  models.ForeignKey('Licencia', on_delete=models.DO_NOTHING, related_name='anunciosLicencia', null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13, null=True)
    descripcion = models.TextField()
    referencia = models.CharField(max_length=50, null=True)
    rutaimagen=models.ImageField(upload_to="anuncios", null=True, blank=True)
    estado = models.CharField(max_length=1,default="A",null=True, blank=True) #activo, inactivo

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.descripcion}'





