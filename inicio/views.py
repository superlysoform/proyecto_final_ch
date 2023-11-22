from datetime import datetime
from typing import Any
from django.db.models.query import QuerySet

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login as django_login 
# from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from inicio.models import Camiseta, Pantalon, Medias

# from inicio.forms import FormularioCreacionUsuario
from inicio.forms import CrearCamisetaForm, CrearPantalonForm, CrearMediasForm, BusquedaCamisetaForm, BusquedaPantalonForm, BusquedaMediasForm, ActualizarCamisetaForm




def inicio(request):
    return render(request, "inicio/inicio.html", {})

def about(request):
    return render(request, "inicio/about.html", {})
    
def pantalones(request):
        
    formulario = BusquedaPantalonForm(request.GET)
    if formulario.is_valid():
        busqueda_marca = formulario.cleaned_data.get("marca")
        listado_de_pantalones = Pantalon.objects.filter(marca__icontains=busqueda_marca)
                 
    formulario = BusquedaPantalonForm()
    return render(request, "inicio/pantalones.html", {"formulario": formulario, "listado_de_pantalones":listado_de_pantalones})


def camisetas(request):
    
    formulario = BusquedaCamisetaForm(request.GET)
    if formulario.is_valid():
        busqueda_marca = formulario.cleaned_data.get("marca")
        listado_de_camisetas = Camiseta.objects.filter(marca__icontains=busqueda_marca)
                 
    formulario = BusquedaCamisetaForm()
    return render(request, "inicio/camisetas.html", {"formulario": formulario, "listado_de_camisetas":listado_de_camisetas})



def medias(request):
    
    formulario = BusquedaMediasForm(request.GET)
    if formulario.is_valid():
        busqueda_marca = formulario.cleaned_data.get("marca")
        listado_de_medias = Medias.objects.filter(marca__icontains=busqueda_marca)
                 
    formulario = BusquedaMediasForm()
    return render(request, "inicio/medias.html", {"formulario": formulario, "listado_de_medias":listado_de_medias})

@login_required  
def crear_camiseta(request):
    
    if request.method == "POST":
        formulario = CrearCamisetaForm(request.POST)
        
        if formulario.is_valid():
            info_limplia = formulario.cleaned_data
        
            marca = info_limplia.get("marca")
            descripcion = info_limplia.get("descripcion")
            equipo = info_limplia.get("equipo")
            anio = info_limplia.get("anio")
            
            camiseta = Camiseta(marca=marca, equipo=equipo, descripcion=descripcion, anio=anio)
            camiseta.save()  
            
            return redirect("camisetas")
        else:
            return render(request, "inicio/crear_camiseta.html", {"formulario":formulario})    
        
    formulario = CrearCamisetaForm()    
    return render(request, "inicio/crear_camiseta.html", {"formulario":formulario})
    
def crear_pantalon(request):
    
    if request.method == "POST":
        formulario = CrearPantalonForm(request.POST)
        
        if formulario.is_valid():
            info_limplia = formulario.cleaned_data
        
            marca = info_limplia.get("marca")
            descripcion = info_limplia.get("descripcion")
            equipo = info_limplia.get("equipo")
            anio = info_limplia.get("anio")
            
            pantalon = Pantalon(marca=marca, equipo=equipo, descripcion=descripcion, anio=anio)
            pantalon.save()  
            
            return redirect("pantalon")
        else:
            return render(request, "inicio/crear_pantalon.html", {"formulario":formulario})    
        
    formulario = CrearPantalonForm()    
    return render(request, "inicio/crear_pantalon.html", {"formulario":formulario})

@login_required  
def crear_medias(request):
    
    if request.method == "POST":
        formulario = CrearMediasForm(request.POST)
        
        if formulario.is_valid():
            info_limplia = formulario.cleaned_data
        
            marca = info_limplia.get("marca")
            descripcion = info_limplia.get("descripcion")
            equipo = info_limplia.get("equipo")
            anio = info_limplia.get("anio")
            
            medias = Medias(marca=marca, equipo=equipo, descripcion=descripcion, anio=anio)
            medias.save()  
            
            return redirect("medias")
        else:
            return render(request, "inicio/crear_medias.html", {"formulario":formulario})    
        
    formulario = CrearMediasForm()    
    return render(request, "inicio/crear_medias.html", {"formulario":formulario})    
    
# @login_required
# def eliminar_camiseta(request, camiseta_id):
#     eliminar_camiseta = Camiseta.objects.get(id=camiseta_id)
#     eliminar_camiseta.delete()
#     return redirect("camisetas")

# @login_required
# def actualizar_camiseta(request, camiseta_id):
#     actualizar_camiseta = Camiseta.objects.get(id=camiseta_id) 
    
#     if request.method == "POST":
#         formulario = ActualizarCamisetaForm(request.POST)
#         if formulario.is_valid():
#             info_nueva = formulario.cleaned_data
            
#             actualizar_camiseta.marca = info_nueva.get("marca")
#             actualizar_camiseta.equipo = info_nueva.get("equipo")
#             actualizar_camiseta.descripcion = info_nueva.get("descripcion")
#             actualizar_camiseta.anio = info_nueva.get("anio")
#             actualizar_camiseta.save()
#             return redirect("camisetas")
#         return render(request, "inicio/actualizar_camiseta.html", {"formulario": formulario})

    
#     formulario = ActualizarCamisetaForm(initial={"marca":actualizar_camiseta.marca, "equipo" :actualizar_camiseta.equipo, "descripcion": actualizar_camiseta.descripcion, "anio":actualizar_camiseta.anio })
#     return render(request, "inicio/actualizar_camiseta.html", {"formulario": formulario})


# def detalle_camiseta(request, camiseta_id):
#     camiseta = Camiseta.objects.get(id=camiseta_id)
#     return render(request, "inicio/detalle_camiseta.html", {"camiseta": camiseta})  

class CamisetaCrearView(LoginRequiredMixin, CreateView):
    model = Camiseta
    template_name = "inicio/crear_camiseta.html"
    fields = ["marca", "equipo", "descripcion", "anio"]
    success_url = reverse_lazy("camisetas")

class ActualizarCamiseta(LoginRequiredMixin, UpdateView):
    model = Camiseta
    template_name = "inicio/actualizar_camiseta.html"
    fields = ["marca", "equipo", "descripcion", "anio"]
    success_url = reverse_lazy("camisetas")

class DetalleCamiseta(LoginRequiredMixin, DetailView):
    model = Camiseta
    template_name = "inicio/detalle_camiseta.html"
    success_url = reverse_lazy("camisetas")

    
class EliminarCamiseta(LoginRequiredMixin, DeleteView):
    model = Camiseta
    template_name = "inicio/eliminar_camiseta.html"
    success_url = reverse_lazy("camisetas")
    
class ListadoCamisetas(ListView):
    model = Camiseta
    context_object_name = "listado_de_camisetas"
    template_name = "inicio/camisetas.html"
    
    def get_queryset(self):
        marca = self.request.GET.get("marca", "")
        if marca:
            listado_de_camisetas = self.model.objects.filter(marca__icontains=marca)
        else:
            listado_de_camisetas = self.model.objects.all()
        return listado_de_camisetas

    
    
    
class DetalleMedias(LoginRequiredMixin, DetailView):
    model = Medias
    template_name = "inicio/detalle_medias.html"

class ActualizarMedias(LoginRequiredMixin, UpdateView):
    model = Medias
    template_name = "inicio/actualizar_medias.html"
    fields = ["marca", "equipo", "descripcion", "anio"]
    success_url = reverse_lazy("medias")

class EliminarMedias(LoginRequiredMixin, DeleteView):
    model = Medias
    template_name = "inicio/eliminar_eliminar.html"
    success_url = reverse_lazy("medias")
    
    
