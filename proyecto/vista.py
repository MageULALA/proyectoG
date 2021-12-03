from django import forms
from django.contrib.auth.models import User
from django.forms.forms import Form
from django.http import HttpResponse
from django.template import Template
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, forms, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from administrador.models import Perfil
from administrador.models import Paquete
from proyecto.carrito import Carrito
from .forms import UserRegistroForm, AnuncioForm
from django.conf import settings
from django.core.mail import send_mail
from django.template import RequestContext

def inicio(request):
    return render(request, 'indexGeneral.html')

def busqueda(request):
    return render(request, 'busqueda.html')

def miperfil(request):
    return render(request, 'PerfilUsuario.html')

def registro(request):
    if request.method == 'POST':
        form = UserRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} registrado')
            usuario = User.objects.get(username=username)
            objPerfil = Perfil.objects.get(user=usuario.pk)            
            enviar_email_registro(form.cleaned_data['email'] , objPerfil.auth_token)
            print(str(form.cleaned_data['email']))
            return redirect('/verificar')
        else:
            messages.success(request, f'Usuario no registrado')
    
    form = UserRegistroForm()
    context = { 'form' : form }
    return render(request, 'registrarme.html', context)

def anunciar(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            form.save()
            messages.success(request, 'Publicado')
            return redirect('inicio')
    else:
        form = AnuncioForm()
        messages.success(request, f'No publicado')

    return render(request, 'anunciar.html', { 'form' : form })

#def enviarToken

def verificar(request):
    return render(request, 'verificarCorreo.html')

def enviar_email_registro(email , auth_token):
    subject = 'Su cuenta necesita ser verificada'
    message = f'Hola Boomero, ingresa a este link para confirmar http://localhost:8000/verificar/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )

def verificado(request, auth_token):
    try:
        objPerfil = Perfil.objects.filter(auth_token = auth_token).first()
        if objPerfil:
            objPerfil.confirmada = True
            objPerfil.save()
            messages.success(request, 'Cuenta verificada exitosamente')
            return redirect('/login')
        else:
            messages.success(request, f'Confirmación fallida. Registrarse nuevamente...')
            return redirect('/registro')
    except Exception as e:
        print(e)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user = authenticate(username=username, password = password)
        
        if new_user is None:
            messages.success(request, 'Datos incorrectos...')
            return redirect('/login')
        else:
            objPerfil = Perfil.objects.filter(user = new_user.pk).first()
            if objPerfil.confirmada:
                login(request, new_user)
                return redirect('inicio')
            else:
                messages.success(request, 'La cuenta no ha sido confirmada.')
                return render(request, 'login.html', {'username':' ','password': ' '})

    else:

        return render(request, 'login.html', {'username':' ','password': ' '})

#
def tienda(request):
    paquetes = Paquete.objects.filter(vigencia="V")
    return render(request, "tienda.html", {'paquetes':paquetes})

def agregar_paquete(request,paquete_id):
    carrito = Carrito(request)
    paquete = Paquete.objects.get(id=paquete_id)
    carrito.agregar(paquete)
    return redirect ('tienda')

def eliminar_paquete(request, paquete_id):
    carrito = Carrito(request)
    paquete= Paquete.objects.get(id=paquete_id)
    carrito.eliminar(paquete)
    return redirect ('tienda')

def restar_paquete(request, paquete_id):
    carrito = Carrito(request)
    paquete= Paquete.objects.get(id=paquete_id)
    carrito.restar(paquete)
    return redirect ('tienda')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('tienda')


