from django.db import models

# Creamos los modelos.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    nombre_usuario = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=50)

class Equipamiento(models.Model):
    tipo_de_equipamiento = models.CharField(max_length=50)
    precio = models.IntegerField()
    accesorios = models.CharField(max_length = 100)

class Replica(models.Model):
    nombre_replica = models.CharField(max_length = 50)
    precio = models.IntegerField()