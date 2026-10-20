from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto

@login_required
def home_page_view(request):
    queryset = Producto.objects.all()
    print(queryset)
    template = "ventas/ventas.html"
    context = {
        "products": queryset
    }
    return render(request, template, context)

def carrito(request):
    return render(request, 'ventas/carrito.html')

def formulario_pedido(request):
    return render(request, 'ventas/formulario_pedido.html')

def product_model_detail_view(request, product_id):
    instance = get_object_or_404(Producto, id = product_id)
    context = {
        "product": instance
    }
    template = "ventas/detail-view.html"
    return render(request, template, context)