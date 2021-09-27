from django.shortcuts import render, get_object_or_404

from .models import Producto, Categoria

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    category_list = Categoria.objects.order_by('nombre')
    context = {
        'product_list': product_list,
        'category_list' : category_list
    }
    return render(request, 'index.html', context)


def producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    producto = get_object_or_404(Producto,pk=producto_id)
    return render(request,'producto.html',{'producto': producto})


def categoria(request, category_id):
    category_list = Categoria.objects.all()
    product_list = Producto.objects.filter(categoria_id = category_id)
    return render(request,'categorias.html',{'product_list' : product_list,'category_list' : category_list})