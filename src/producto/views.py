from django.shortcuts import render
from producto.models import Categoria

# Vista para mostrar categorías y productos
def categoria_productos_view(request):
    # Obtener todas las categorías
    categorias = Categoria.objects.all()
    return render(request, 'categoria_productos.html', {'categorias': categorias})