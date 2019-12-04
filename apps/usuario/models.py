from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.producto.models import zapatilla

# Create your models here.


class perfilUsuario (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil=models.ImageField(upload_to='foto_perfil',blank=True)
    def __str__(self):
        return self.user.name
    



class compra (models.Model):
    id_compra = models.IntegerField(primary_key=True)
    producto = models.ForeignKey(
        zapatilla, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField
    fecha_compra = models.DateField (null=True) 
    hora_compra = models.TimeField (null=True)
    persona = models.ForeignKey (
        perfilUsuario, null=True, blank=True, on_delete=models.CASCADE)

