from django.urls import path
from .views import Home,NuevoProductos

urlpatterns = [
    path('',Home,name='home'),
    path('Agregar/',NuevoProductos,name="agregar")
]  