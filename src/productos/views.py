from django.shortcuts import render
from productos.models import Categoria


# Vista para mostrar categorías y productos
def categoria_productos_view(request):
    # Obtener todas las categorías
    categorias = Categoria.objects.all()
    return render(request, 'productos/categoria_productos.html', {'categorias': categorias})
#reverse('productos:categorias_productos')
