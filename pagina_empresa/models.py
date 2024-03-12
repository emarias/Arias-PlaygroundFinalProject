from django.db import models

class Empleado(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    sector= models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.apellido} {self.nombre} - {self.sector}"