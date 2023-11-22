from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login 
from django.contrib.auth.views import PasswordChangeView

from cuentas.forms import FormularioCreacionUsuario, EditarPerfilForm
from cuentas.models import DatosExtra

from django.urls import reverse_lazy




# Cuentas / Usuario #

def login(request):
    
    formulario = AuthenticationForm()

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.cleaned_data.get("username")
            pwd = formulario.cleaned_data.get("password")
            user = authenticate(username=user , password=pwd)
            
            django_login(request, user) 
            
            DatosExtra.objects.get_or_create(user=request.user)

            return redirect("inicio")

    return render(request, "cuentas/login.html", {"form_login":formulario})


def registro(request):
    formulario = FormularioCreacionUsuario()
    
    if request.method == "POST":  
        formulario = FormularioCreacionUsuario(request.POST) 
        if formulario.is_valid():
            formulario.save()
            return redirect("login")    
    
    return render(request, "cuentas/registro.html", {"form_registro":formulario})

def editar_perfil(request):
    
    datos_extra = request.user.datosextra
        
    formulario = EditarPerfilForm(instance=request.user, initial={"bio" : datos_extra.bio, "avatar" : datos_extra.avatar})
    
    if request.method == "POST":  
        formulario = EditarPerfilForm(request.POST, request.FILES, instance=request.user) 
        
        if formulario.is_valid():
            
            nueva_bio = formulario.cleaned_data.get("bio")
            nuevo_avatar = formulario.cleaned_data.get("avatar")

            
            if nueva_bio:
               datos_extra.bio = nueva_bio
               
            if nuevo_avatar:
               datos_extra.avatar = nuevo_avatar
              
               datos_extra.save()   
               formulario.save()
               
            return redirect("editar_perfil")

    
    return render(request, "cuentas/editar_perfil.html",{"form_editar":formulario})

class CambiarContraseña(PasswordChangeView):
    template_name = "cuentas/cambiar_pwd.html"
    success_url = reverse_lazy("editar_perfil")
    
    
class Perfil(ListView):
    model = DatosExtra 
    template_name = "cuentas/perfil.html"
    success_url = reverse_lazy("perfil")