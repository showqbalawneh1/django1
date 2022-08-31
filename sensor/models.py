from django.db import models
from datetime import datetime 


# Create your models here.

class pressureSensor(models.Model):
    labelSensor =models.CharField(max_length=200)
    installationDate=models.DateTimeField(auto_now_add=True)
    longitude= models.DecimalField(max_digits=9,decimal_places=6)
    latitude=models.DecimalField(max_digits=9,decimal_places=6)
    def __str__(self):
        return self.labelSensor
    
    
class sensorReading (models.Model):
    sensor=models.ForeignKey(pressureSensor, on_delete=models.CASCADE,null=False)
    readingDate=models.DateTimeField(auto_now_add=True)
    value=models.DecimalField(max_digits=19,decimal_places=10)
 