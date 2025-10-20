from django.db import models

# Create your models here.

class Medicamento(models.Model):
    id_proveedor = models.IntegerField()
    nombre = models.CharField(max_length=50)
    funcion = models.CharField(max_length=150)
    presentacion = models.CharField(max_length=50)
    precio = models.FloatField()
    stock = models.IntegerField()
    f_caducidad = models.DateField()
    

    def __str__(self):
        return f'Medicamento: {self.nombre} {self.funcion}'