from django.db.models.signals import post_save
from administrador.models import Perfil
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
