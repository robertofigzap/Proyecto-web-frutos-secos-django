from django.db import models
from django.db.models.fields import IntegerField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Despacho(models.Model):
    numerodespacho = models.IntegerField()
    nombrecliente = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    productos = models.ForeignKey(Producto, on_delete=models.PROTECT)
    peso = models.CharField(max_length=30)
    medidas = models.CharField(max_length=30)
    fechaingreso = models.DateField()
    fechaentrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return self.nombrecliente