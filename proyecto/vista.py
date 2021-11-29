from django import forms
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import Template
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, forms, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from administrador.models import Perfil
from .forms import UserRegistroForm, AnuncioForm

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

def anunciar(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = AnuncioForm(request.POST)
        if form.is_valid():
            #post = form.save(commit=False)
            form.user = current_user
            form.save()
            messages.success(request, 'Publicado')
            return redirect('inicio')
    else:
        form = AnuncioForm()
        messages.success(request, f'No publicado')

    return render(request, 'anunciar.html', { 'form' : form })






