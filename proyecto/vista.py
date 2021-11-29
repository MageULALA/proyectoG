from django import forms
from django.http import HttpResponse
from django.template import Template
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, forms, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistroForm

def inicio(request):
    return render(request, 'indexGeneral.html')

def perfil(request):
    return render(request, 'PerfilUsuario.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} registrado')
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('inicio')
    else: 
        form = UserRegistroForm()
        messages.success(request, f'Usuario no registrado')

    context = { 'form' : form }
    return render(request, 'registrarme.html', context)

def busqueda(request):
    return render(request, 'busqueda.html')

def miperfil(request):
    return render(request, 'PerfilUsuaio.html')




