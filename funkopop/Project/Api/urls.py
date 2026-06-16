from django.urls import path
from .views import Catalogo, DetalleProducto, Home, NuevoProductos

urlpatterns = [
    path('', Home, name='home'),
    path('catalogo/', Catalogo, name='catalogo'),
    path('producto/<int:codigo>/', DetalleProducto, name='detalle_producto'),
    path('Agregar/', NuevoProductos, name="agregar"),
]
