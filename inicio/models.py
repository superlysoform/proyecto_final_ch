from django.db import models
from django.contrib.auth.models import User
# from ckeditor

class Camiseta(models.Model):
    marca = models.CharField(max_length=30)
    equipo = models.CharField(max_length=30) 
    descripcion = models.TextField() 
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.marca} - {self.equipo} - {self.descripcion} - {self.anio}"
    

class Pantalon(models.Model):
    marca = models.CharField(max_length=30)
    equipo = models.TextField() 
    descripcion = models.TextField() 
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.marca} - {self.equipo} - {self.descripcion} - {self.anio}"
    
class Medias(models.Model):
    marca = models.CharField(max_length=30)
    equipo = models.TextField() 
    descripcion = models.TextField() 
    anio = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.marca} - {self.equipo} - {self.descripcion} - {self.anio}"    

class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    
    
    
    
    
    
    
    