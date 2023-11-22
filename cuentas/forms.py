from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class FormularioCreacionUsuario(UserCreationForm):
    email = forms.EmailField(label="Ingrese Email")
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        
class EditarPerfilForm(UserChangeForm):
    email = forms.EmailField(label="Cambiar Email")
    password = None
    first_name = forms.CharField(label="Cambiar Nombre", required= False)  
    last_name = forms.CharField(label="Cambiar Apeliido", required= False)
    bio = forms.CharField(label="Biografia", required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "bio","avatar"]
