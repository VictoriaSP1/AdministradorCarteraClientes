from django.db import models


class Agente (models.Model):
    Nombre_Agente = models.CharField(max_length=200)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.Nombre_Agente}"
    
    

class Cliente (models.Model):
    Nombre_Cliente = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)
    Id_Agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.Nombre_Cliente} {self.Id_Agente.Nombre_Agente}"
    

class Asegurado (models.Model):
    Nombre_Asegurado = models.CharField(max_length=200)
    Edad = models.IntegerField()
    
    def __str__(self):
        return f"{self.Nombre_Asegurado}"
            


class Tipo_Poliza (models.Model):
    Tipo_Poliza = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.Tipo_Poliza}"


class Estado_Poliza (models.Model):
    Estado_Poliza = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.Estado_Poliza}"


class Poliza_Asegurado (models.Model):
    Id_Asegurado = models.ForeignKey(Asegurado, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.Id_Asegurado.Nombre_Asegurado}"
    

class Poliza (models.Model):
    Num_Poliza = models.IntegerField()
    Fecha_Inicio = models.DateField()
    Fecha_Vigencia = models.DateField()
    Id_Cliente = models.ForeignKey (Cliente, on_delete=models.CASCADE)
    Id_Asegurado = models.ForeignKey(Poliza_Asegurado, on_delete=models.CASCADE)
    Aseguradora = models.CharField(max_length=200)
    Tipo_Poliza = models.ForeignKey(Tipo_Poliza, on_delete=models.CASCADE)
    Precio = models.FloatField()
    Estado_Poliza = models.ForeignKey(Estado_Poliza, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%d: %s' % (
            self.Id_Cliente.Nombre_Cliente, 
            self.Id_Asegurado.Id_Asegurado.Nombre_Asegurado,
            self.Tipo_Poliza.Tipo_Poliza,
            self.Estado_Poliza.Estado_Poliza
            )
        



