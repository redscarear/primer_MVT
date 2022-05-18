from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    parentesco = models.CharField(max_length=40)
    edad = models.IntegerField()
