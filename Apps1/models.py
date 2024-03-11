from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Gender(models.Model):
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.gender

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    Card = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.fullname