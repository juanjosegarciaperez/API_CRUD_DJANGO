from django.db import models

# Create your models here.

class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=True)
    phone = models.CharField(max_length=10, null=True, default=True)
    is_active = models.BooleanField(default=True)
    
    
class student(models.Model):
    name = models.CharField(max_length=50)
    lastname= models.CharField(max_length=30)
    sex = models.CharField(max_length=1)
    Numficha = models.PositiveIntegerField(default=True)
    Formacion = models.BooleanField(default=True)
    FechaFormacion = models.DateField()
    is_active = models.BooleanField(default=True)