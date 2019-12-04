from django.urls import path, include
from . import views

from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
     
urlpatterns = [
    path('basic/', views.API_objects.as_view()),
    path('basic/<int:pk>/', views.API_objects_details.as_view()),
]     


urlpatterns += [   
    path('', views.home),
    path('listar_productos',views.listar_productos),
    path('editar_producto/<int:codigo>', views.editar_producto),
    path('borrar_producto/<int:codigo>', views.borrar_producto),
    #path('agregarProducto',views.inscripcion_producto),
    path('page', views.inicio),
]
