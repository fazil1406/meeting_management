from django.db import models

# Create your models here.
class register(models.Model):
    First_name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Username=models.CharField(max_length=100,unique=True)
    Email=models.EmailField(max_length=300,unique=True)
    Password=models.CharField(max_length=100,unique=True)
    Confirmpassword=models.CharField(max_length=100,unique=True)

    class Meta:
        db_table='Register'



    
