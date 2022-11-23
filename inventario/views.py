from django.shortcuts import render
from inventario.models import Productos
from django.http import HttpResponse

# Create your views here.

def pagina(request):
    return render(request, "pagina_principal.Html")

def producto(request):
    return render(request, "productos.html")

def cliente(request):
    return render(request, 'usuario.html')