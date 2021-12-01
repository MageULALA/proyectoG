from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from administrador.models import Anuncio
from administrador.models import Departamento, Servicio

class UserRegistroForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo eléctronico', required=True)
    password1 = forms.CharField(label='Crea una contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, label='Ingresa tus nombres')


    class Meta:
        model = User
        fields = ['first_name','username','email','password1', 'password2' ]
        help_texts = {k:"" for k in fields }

class AnuncioForm(forms.ModelForm): 
    titulo = forms.CharField(label="Titulo", required=True)
    telefono = forms.CharField(label="Telefono", required=True)
    descripcion = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿De qué trata el anuncio?'}), required=True)
    referencia = forms.CharField(label="Referencia", required=True)
    rutaimagen = forms.ImageField(label="Foto", required=False)
    servicio = forms.ModelChoiceField(label="Tipo servicio", queryset=Servicio.objects.all(),  required=True)
    departamento = forms.ModelChoiceField(label="Departamento", queryset=Departamento.objects.all(),  required=True)
        
    class Meta:
        model = Anuncio
        fields = ['titulo','servicio', 'descripcion','telefono','departamento','referencia', 'rutaimagen' ]



