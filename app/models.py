from django.db import models

# Create your models here.
class Poliza (models.Model):
    Num_Poliza = models.IntegerField()
    Fecha_Inicio = models.DateField()
    Fecha_Vigencia = models.DateField()
    Id_Cliente = models.ForeignKey (Cliente, on_delete=models.CASCADE)
    Id_Asegurado = models.ForeignKey(Asegurado, on_delete=models.CASCADE)
    Aseguradora = models.CharField(max_length=200)
    Tipo_Poliza = models.ForeignKey(Tipo_Poliza, on_delete=models.CASCADE)
    Precio = models.DecimalField()
    Estado_Poliza = models.ForeignKey(Estado_Poliza, on_delete=models.CASCADE)

class Cliente (models.Model):
    Nombre_Cliente = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)
    Id_Agente = models.ForeignKey(Agente, on_delete=models.CASCADE)

class Agente (models.Model):
    Nombre_Agente = models.CharField(max_length=200)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

class Poliza_Asegurado:
    Id_Asegurado = models.ForeignKey(Asegurado, on_delete=models.CASCADE)
    
class Asegurado (models.Model):
    Nombre_Asegurado = models.CharField(max_length=200)
    Edad = models.IntegerField()
    
class Tipo_Poliza (models.Model):
    Tipo_Poliza = models.CharField(max_length=200)

class Estado_Poliza (models.Model):
    Estado_Poliza = models.CharField(max_length=50)