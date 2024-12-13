from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del ingrediente
    descripcion = models.TextField(null=True, blank=True)  # Descripción opcional del ingrediente
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)  # Cantidad del ingrediente
    unidad = models.CharField(max_length=50)  # Unidad de medida (gramos, ml, etc.)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ingredientes')  # Relación con el producto

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} {self.unidad}"