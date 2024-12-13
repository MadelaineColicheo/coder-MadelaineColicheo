from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
