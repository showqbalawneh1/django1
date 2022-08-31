from rest_framework import generics
from .models import pressureSensor,sensorReading
from .serializers import pressureSensorSer, sensorReadingSer
from datetime import datetime 


class pressureSensorVS(generics.ListAPIView):
    queryset=pressureSensor.objects.all()
    serializer_class=pressureSensorSer
    
class sensorReadingVS(generics.ListAPIView):
    queryset=sensorReading.objects.filter(readingDate__range=["2020-01-01", "2020-12-31"])
    serializer_class= sensorReadingSer                        