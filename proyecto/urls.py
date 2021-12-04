"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import template
from django.contrib import admin
from django.contrib.auth import login
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', vista.inicio, name='inicio'),
    path('registro/', vista.registro, name='registro'),
    path('login/', vista.loginUser, name='login'),
    path('logout/', LogoutView.as_view(template_name='indexGeneral.html'), name='logout'),
    path('busqueda/', vista.busqueda, name='busqueda'),
    path('perfil/', vista.miperfil, name='perfil'),
    path('anunciar/', vista.anunciar, name='anunciar'),
    path('verificar/', vista.verificar, name='verificar'),
    path('verificar/<auth_token>/', vista.verificado, name='verificado'),
    path('tienda/', vista.tienda, name='tienda'),
    path('agregar/<int:paquete_id>/', vista.agregar_paquete, name='Add'),
    path('eliminar/<int:paquete_id>/', vista.eliminar_paquete, name='Del'),
    path('restar/<int:paquete_id>/', vista.restar_paquete, name='Sub'),
    path('limpiar/', vista.limpiar_carrito, name='CLS'),
    path('anunciosPerfil/', vista.anunciosPerfil, name='anunciosPerfil'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

