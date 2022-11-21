from django.shortcuts import render
from inventario.models import Productos
from django.http import HttpResponse

# Create your views here.

def busqueda_producto(request):
    return render(request, "buscar_producto.html")