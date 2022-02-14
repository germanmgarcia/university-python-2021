from importlib.util import module_for_loader
from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
