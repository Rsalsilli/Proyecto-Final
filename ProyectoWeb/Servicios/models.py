from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorias(models.Model):
    nombreCat= models.CharField(max_length=30)
    imagenCat= models.ImageField(upload_to='categoria')
    def __str__(self):
        return self.nombreCat

class Streamers(models.Model):
    nombre=models.CharField(max_length=30)
    followers=models.IntegerField()
    imagen=models.ImageField(upload_to='servicios')
    canalLink=models.CharField(max_length=100)
    categorias = models.ManyToManyField(Categorias)
    peakViewers=models.IntegerField()
    followerChange=models.IntegerField()
    hoursViewers= models.IntegerField()
    
    def __str__(self):
        return self.nombre


