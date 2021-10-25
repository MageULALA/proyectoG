from django.db import models

# Create your models here.
class Servicio(models.Model):
    idServicio=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=80)
    vigencia = models.BooleanField()
    def __str__(self):
        return self.descripcion

class Foto(models.Model):
    idFoto=models.AutoField(primary_key=True)
    ruta=models.ImageField(upload_to="anuncios", null=True) #se crea dentro de media
    idAnuncio = models.ForeignKey('Anuncio',on_delete=models.DO_NOTHING)

class Tarjeta(models.Model):
    idTarjeta=models.AutoField(primary_key=True)
    nombreTarjeta=models.CharField(max_length=50)
    numeroTarjeta=models.CharField(max_length=19)
    fechaExpiracion=models.DateField()
    cvc=models.CharField(max_length=4)
    idUsuario= models.ForeignKey('Usuario',on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nombreTarjeta

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=20)
    cuenta = models.EmailField(max_length=200,unique=True)
    telefono = models.CharField(max_length=13)
    descripcionUsuario= models.CharField(max_length=200,null=True)
    ruta_foto= models.ImageField(upload_to="usuarios", null=True) #se crea dentro de media
    def __str__(self):
        return self.nombres
class Anuncio(models.Model):
    idAnuncio = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    descripcion=models.CharField(max_length=255)
    telefono=models.CharField(max_length=13)
    departamento = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    idServicio = models.ForeignKey('Servicio',on_delete=models.DO_NOTHING)
    idUsuario = models.ForeignKey('Usuario',on_delete=models.DO_NOTHING)
    idLicencia = models.ForeignKey('Licencia',on_delete=models.DO_NOTHING)
    vigencia = models.BooleanField()
    permitido = models.BooleanField()

class Seguidor(models.Model):
    id = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey('Usuario',on_delete=models.DO_NOTHING, related_name='usuarioPrincipal')
    idUsuarioSeguidor=models.ForeignKey('Usuario',on_delete=models.DO_NOTHING, related_name='usuarioSeguidor')

class Favorito(models.Model):
    id = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey('Usuario',on_delete=models.DO_NOTHING)
    idAnuncio = models.ForeignKey('Anuncio',on_delete=models.DO_NOTHING)
    fecha_guardado= models.DateField()

class Paquete(models.Model):
    idPaquete = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    cantidadAnuncios = models.SmallIntegerField(default=1)
    duracionDias = models.SmallIntegerField()
    precio = models.DecimalField(decimal_places=2,max_digits=6)
    vigencia = models.BooleanField()
    def __str__(self):
        return self.descripcion

class Venta(models.Model):
    idVenta=models.AutoField(primary_key=True)
    fecha= models.DateField()
    hora= models.TimeField()
    descuento = models.DecimalField(decimal_places=2,max_digits=3)
    total = models.DecimalField(decimal_places=2,max_digits=6) #aplicadpo el dscto.
    idTarjeta=models.ForeignKey('Tarjeta',on_delete=models.DO_NOTHING)

class Licencia(models.Model):
    idLicencia=models.AutoField(primary_key=True)
    idPaquete = models.ForeignKey('Paquete',on_delete=models.DO_NOTHING)
    idVenta = models.ForeignKey('Venta',on_delete=models.DO_NOTHING)
    fecha_inicio=models.DateField(null=True)
    fecha_fin=models.DateField(null=True)
    estado = models.BooleanField() #activo, programado, expirado
