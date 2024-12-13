# productos/urls.py
from django.urls import path
from . import views

app_name = 'productos'  # Definir un espacio de nombres para la aplicación

urlpatterns = [
    path('', views.categoria_productos_view, name='categorias_productos'),
]
