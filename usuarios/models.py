from django.db import models
from django.contrib.auth.models import User

class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True,blank=True)
    tipo_de_sangre = models.CharField(max_length=5, blank=True, null=True)
    
    def __str__(self):
        return f'Datos extra del usuario {self.user}'