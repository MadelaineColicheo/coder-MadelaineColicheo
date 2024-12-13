from django.shortcuts import render
from .models import Categoria, Producto

# Vista para mostrar categorías y productos
def categoria_productos_view(request):
    # Obtener todas las categorías
    categorias = Categoria.objects.all()

    # Obtener los productos asociados a cada categoría
    # En Django, podemos acceder a los productos de una categoría usando la relación definida en el modelo.
    
    return render(request, 'categoria_productos.html', {'categorias': categorias})