# Generated by Django 3.2.7 on 2021-12-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_alter_anuncio_rutaimagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='auth_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='confirmada',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
