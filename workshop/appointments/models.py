

from django.db import models

# Create your models here.


    
class Car(models.Model):
    carName = models.CharField(max_length=60)
    
    
    
    
class Appointment(models.Model):
    customerName= models.CharField(max_length=60)
    date = models.DateField()
    car = models.ForeignKey(Car,on_delete=models.CASCADE)

    owner = models.ForeignKey('auth.user', related_name='appointments', on_delete=models.CASCADE)