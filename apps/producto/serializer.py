# este archivo nos ayudara a convertir los 
# objetos en json y viceversa

from .models import zapatilla
from rest_framework import serializers

#vamos a definir que campos vamos a transmitir
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= zapatilla
        fields = '__all__'
