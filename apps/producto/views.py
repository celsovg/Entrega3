from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import zapatilla
from .forms import ProductoForm

from .serializer import ProductoSerializer
from rest_framework import generics

class API_objects(generics.ListCreateAPIView):
        queryset= zapatilla.objects.all()
        serializer_class = ProductoSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset= zapatilla.objects.all()
        serializer_class = ProductoSerializer


def inicio(request):
    return render(request, '/templates/old/indice.html', {})


# Create your views here.
def home(request):
    return render(request, 'templates/base.html', {})


def listar_productos(request):
    # creamos una colección la cual carga TODOS los registos
    productos = zapatilla.objects.all()
    # renderizamos la colección en el template
    return render(request,
        "templates/listar_productos.html", {'productos': productos})

def editar_producto(request, codigo):
    # Recuperamos el registro de la base de datos por el id
    instancia= zapatilla.objects.get(id=codigo)
    # creamos un formulario con los datos del objeto
    form=  ProductoForm(instance=instancia)
    # Compronbamos si se envió el formulario
    if request.method=="POST":
        # Actualizamos el formulario con los datos del objeto
        form= ProductoForm(request.POST, instance=instancia)
        # Si el formulario es valido....
        if form.is_valid():
            #Guardamos el formulario pero sin confirmar aun
            instancia= form.save(commit=False)
            # grabamos!!!
            instancia.save()
    return render(request, "app/editar_producto.html",{'form':form})            

def borrar_producto(request, codigo):    
    instacia= zapatilla.objects.get(id=codigo)
    instacia.delete()
    return redirect('/')