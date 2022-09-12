from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime 
import django_filters
import uuid


# Create your models here.

class pressureSensor(models.Model):
    def validation(labelSensor):
        str = [*labelSensor]
        if("PSSR" not in labelSensor[0:4]):
            raise ValidationError(('labelSensor not valid should has a PSSR prefix '))

    labelSensor =models.CharField(max_length=200,validators=[validation])
    installationDate=models.DateTimeField(auto_now_add=True)
    longitude= models.DecimalField(max_digits=9,decimal_places=6)
    latitude=models.DecimalField(max_digits=9,decimal_places=6)
    serial_number=models.CharField(max_length=200,default=uuid.uuid4,editable=False)
    
 

    def __str__(self):
        return self.labelSensor
    
    
class sensorReading (models.Model):
    sensor=models.ForeignKey(pressureSensor, on_delete=models.CASCADE,null=False)
    readingDate=models.DateTimeField(auto_now_add=True,editable=False)
    value=models.DecimalField(max_digits=19,decimal_places=10)
 
 
