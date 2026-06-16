from django.shortcuts import get_object_or_404, render
from .forms import *
from django.contrib.auth.decorators import permission_required
from .models import Producto

# Create your views here.
def Home(request):
    productos_destacados = Producto.objects.order_by('-Codigo')[:4]
    return render(request, 'base.html', {
        'productos_destacados': productos_destacados,
    })


def Catalogo(request):
    productos = Producto.objects.order_by('Nombre')
    consulta = request.GET.get('q', '').strip()
    categoria = request.GET.get('categoria', '').strip()

    if consulta:
        productos = productos.filter(Nombre__icontains=consulta)

    if categoria:
        productos = productos.filter(Categoria__iexact=categoria)

    categorias = (
        Producto.objects.order_by('Categoria')
        .values_list('Categoria', flat=True)
        .distinct()
    )

    return render(request, 'Pages/catalogo.html', {
        'productos': productos,
        'categorias': [item for item in categorias if item],
        'consulta': consulta,
        'categoria_actual': categoria,
    })


def DetalleProducto(request, codigo):
    producto = get_object_or_404(Producto, Codigo=codigo)
    relacionados = (
        Producto.objects.exclude(Codigo=producto.Codigo)
        .order_by('-Codigo')[:3]
    )
    return render(request, 'Pages/detalle_producto.html', {
        'producto': producto,
        'relacionados': relacionados,
    })


@permission_required('Api.add_producto')
def NuevoProductos(request):
    data = {
        'Formulario': FormularioProductos()
    }
    if request.method == 'POST':
        formulario = FormularioProductos(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['Formulario'] = FormularioProductos()
            data['Mensaje'] = "Producto Guardado Correctamente"
        else:
            data['Formulario'] = formulario
            data['Mensaje'] = "Error al Guardar el Producto"
    return render(request, 'Pages/NuevoProducto.html', data)
