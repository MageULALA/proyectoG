from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

