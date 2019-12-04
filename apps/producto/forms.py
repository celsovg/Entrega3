from django import forms
from .models import zapatilla

class FotoZapatillaForm(forms.ModelForm):
    class Meta():
        model = zapatilla
        fields = ('foto_zapatilla',)
        labels = { 'zapatilla':'Foto del producto' }
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model= zapatilla
        fields= ['codigo', 'marca', 'modelo', 'precio', 'stock']
