from django.db import models
from ckeditor.fields import RichTextField

class Empleado(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    sector= models.CharField(max_length=30)
    sobre_mi= RichTextField(null=True)
    imagen = models.ImageField(upload_to='empleados_images', null=True, blank=True)
    
    def __str__(self):
        return f"{self.apellido} {self.nombre} - {self.sector}"