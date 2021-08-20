from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField("nombre",blank=False,max_length=100)
    edad = models.IntegerField("edad",blank=False)
    
    def __str__(self):
        return self.nombre