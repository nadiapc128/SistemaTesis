from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=50)
	edad = models.IntegerField()
	genero = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=50)
	id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class Hola(models.Model):
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=50)
	edad = models.IntegerField()
	genero = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=50)
	id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

