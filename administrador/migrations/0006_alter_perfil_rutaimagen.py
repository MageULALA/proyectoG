# Generated by Django 3.2.7 on 2021-11-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0005_auto_20211128_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='rutaimagen',
            field=models.ImageField(blank=True, default='/static/fotonn.png', null=True, upload_to='usuarios'),
        ),
    ]
