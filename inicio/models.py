from django.db import models
from ckeditor.fields import RichTextField

class Camiseta(models.Model): 
    marca = models.CharField(max_length=30)
    equipo = models.CharField(max_length=30) 
    descripcion = RichTextField()
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
    descripcion = RichTextField() 
    anio = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.marca} - {self.equipo} - {self.descripcion} - {self.anio}"    


    
    
    
    
    
    
    
    