from rest_framework import serializers
from .models import pressureSensor,sensorReading 

class pressureSensorSer(serializers.ModelSerializer):
    class Meta :
        model=pressureSensor
        fields =('labelSensor','installationDate','longitude','latitude')
        
class sensorReadingSer(serializers.ModelSerializer):
    class Meta :
        model=sensorReading
        fields =('sensor','readingDate','value')
        