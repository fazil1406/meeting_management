from django.db import models

# Create your models here.
class register(models.Model):
    Username=models.CharField(max_length=100,unique=True)
    Email=models.EmailField(max_length=300,unique=True)
    Password=models.CharField(max_length=100,unique=True)
    Confirmpass=models.CharField(max_length=100,unique=True)

