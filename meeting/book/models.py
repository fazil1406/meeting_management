from django.db import models

# Create your models here.
class Booking(models.Model):
    host_name=models.CharField(max_length=200)
    class_name=models.CharField(max_length=100)
    students=models.IntegerField()
    subject=models.CharField(max_length=100)
    timing=models.TimeField(auto_now=False, auto_now_add=False,)

    class Meta:
        db_table="Booking"