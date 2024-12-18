# Generated by Django 5.1.3 on 2024-12-13 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unidad', models.CharField(max_length=50)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='productos.producto')),
            ],
        ),
    ]
