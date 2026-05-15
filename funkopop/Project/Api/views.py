from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import permission_required

# Create your views here.
def Home(request):
    return render (request,'Base.html')
@permission_required('Api.add_producto')

def NuevoProductos(request):
    data={
        'Formulario': FormularioProductos()
    }
    if request.method == 'POST':
        formulario = FormularioProductos(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['Mensaje'] = "Producto Guardado Correctamente"
        else:
            data['Mensaje'] = "Error al Guardar el Producto"
    return render(request, 'Pages/NuevoProducto.html', data)