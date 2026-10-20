from django.db import models

# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    