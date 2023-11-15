from django.contrib import admin
from inicio.models import Camiseta

admin.site.register(Camiseta)

def __str__(self):
    return f"(self.id) - (self.marca) - (self.equipo) - (self.descripcion) - (self.anio)"
