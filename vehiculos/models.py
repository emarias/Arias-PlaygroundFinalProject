from django.db import models
from ckeditor.fields import RichTextField

class Autos(models.Model):
    modelo= models.CharField(max_length=30)
    color= models.CharField(max_length=30)
    marca= models.CharField(max_length=30)
    fecha_de_fabricacion= models.DateField()
    descripcion= RichTextField(null=True)
    imagen = models.ImageField(upload_to='autos_images', null=True, blank=True)
    
    def __str__(self):
        return f"{self.modelo} {self.marca} - {self.color}"