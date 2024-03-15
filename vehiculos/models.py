from django.db import models

class Autos(models.Model):
    modelo= models.CharField(max_length=30)
    color= models.CharField(max_length=30)
    marca= models.CharField(max_length=30)
    fecha_de_fabricacion= models.DateField()
    
    def __str__(self):
        return f"{self.modelo} {self.marca} - {self.color}"