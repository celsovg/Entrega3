from django.db import models
from django.utils import timezone


# Create your models here.
class zapatilla(models.Model):
    codigo = models.IntegerField (primary_key=True)
    marca = models. CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=6, decimal_places=3)
    foto_zapatilla=models.ImageField(upload_to='foto_zapatilla',blank=True)
    stock = models.IntegerField(null=True)
    
