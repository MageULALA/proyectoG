# Generated by Django 3.2.7 on 2021-11-28 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=80)),
                ('cantidadAnuncios', models.SmallIntegerField(default=1)),
                ('duracionDias', models.SmallIntegerField(default=6)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vigencia', models.CharField(blank=True, default='V', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('vigencia', models.CharField(blank=True, default='V', max_length=1)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTarjeta', models.CharField(max_length=30)),
                ('numeroTarjeta', models.CharField(max_length=19)),
                ('fechaExpiracion', models.DateField()),
                ('cvc', models.CharField(max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarjetasUsuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ventasTarjeta', to='administrador.tarjeta')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(null=True)),
                ('fecha_fin', models.DateField(null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('estado', models.CharField(blank=True, default='A', max_length=1, null=True)),
                ('paquete', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='licenciasPaquete', to='administrador.paquete')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='licenciasVenta', to='administrador.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('referencia', models.CharField(max_length=50)),
                ('rutaimagen', models.ImageField(upload_to='anuncios')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='anunciosDepartamento', to='administrador.departamento')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='anunciosServicio', to='administrador.servicio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anunciosUsuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
