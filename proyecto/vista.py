from django.http import HttpResponse
from django.template import Template, Context, context
from django.shortcuts import render

def inicio(request):
    return render(request, 'indexGeneral.html')

def perfil(request):
    return render(request, 'PerfilUsuario.html')

def registro(request):
    return render(request, 'registrarme.html')

