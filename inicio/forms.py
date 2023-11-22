from django import forms
from ckeditor.fields import RichTextFormField

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User


# class FormularioCreacionUsuario(UserCreationForm):
#     email = forms.EmailField(label="Ingrese Correo")
#     password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]
    
# class EditarPerfilForm(UserChangeForm):
#     email = forms.EmailField(label="Cambiar Email")
#     password = None
#     first_name = forms.CharField(label="Cambiar Nombre", required= False)  
#     last_name = forms.CharField(label="Cambiar Apeliido", required= False)
#     bio = forms.CharField(label="Biografia", required=False)
#     avatar = forms.ImageField(required=False)
    

#     class Meta:
#         model = User
#         fields = ["email", "first_name", "last_name", "bio","avatar"]



class BaseCamisetaForm(forms.Form):
    marca = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    anio = forms.DateField()
    
    
class CrearCamisetaForm(forms.Form):
    marca = forms.CharField(max_length=30)
    equipo = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    anio = forms.IntegerField()
    
class CrearPantalonForm(BaseCamisetaForm):
    ...
    
class CrearMediasForm(BaseCamisetaForm):
    ...
    
    
class BusquedaCamisetaForm(forms.Form):
    marca = forms.CharField(max_length=30, required=False)

class BusquedaPantalonForm(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    
class BusquedaMediasForm(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    
class ActualizarCamisetaForm(forms.Form):
    marca = forms.CharField(max_length=10)
    equipo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    
    
class ActualizarMediasForm(forms.Form):
    marca = forms.CharField(max_length=20)
    equipo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    