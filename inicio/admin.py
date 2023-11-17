from django.contrib import admin
from inicio.models import Camiseta, Medias, Pantalon

admin.site.register([Camiseta, Medias, Pantalon])

def __str__(self):
    return f"(self.id) - (self.marca) - (self.equipo) - (self.descripcion) - (self.anio)"


