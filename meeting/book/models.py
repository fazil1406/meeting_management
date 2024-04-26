from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Booking(models.Model):
    host_name=models.CharField(max_length=200)
    class_name=models.CharField(max_length=100)
    students=models.IntegerField()
    subject=models.CharField(max_length=100)
    starttiming=models.TimeField(auto_now=False, auto_now_add=False)
    endtiming=models.TimeField(auto_now=False, auto_now_add=False)
    Datee=models.DateField(default=datetime.date.today)
    Durations=models.DurationField(default=timezone.timedelta(hours=1))
    
    class Meta:
         db_table="Booking"

    