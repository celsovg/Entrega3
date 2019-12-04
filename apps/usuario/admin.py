from django.contrib import admin
from apps.usuario.models import compra
from apps.usuario.models import perfilUsuario, compra

# Register your models here.


admin.site.register(compra)
admin.site.register(perfilUsuario)