from rest_framework import generics
from .models import pressureSensor,sensorReading
from .serializers import pressureSensorSer, sensorReadingSer
from datetime import datetime 
from django_filters import rest_framework as filters


class pressureSensorFilter(filters.FilterSet):
    class Meta:
        model=pressureSensor
        fields={
            'labelSensor':['icontains'],
            'installationDate':['lte']
        }
class pressureSensorVS(generics.ListAPIView):
    queryset=pressureSensor.objects.all()
    serializer_class=pressureSensorSer
    filterset_class=pressureSensorFilter
    
class sensorReadingFilter(filters.FilterSet):
    name = filters.NumberFilter(field_name="value", lookup_expr='lte')
    name = filters.DateTimeFilter(field_name="readingDate", input_formats=['%Y-%m-%d','%d-%m-%Y'],lookup_expr='icontains')
    class Meta:
        model=sensorReading
        fields=('sensor','readingDate')
class sensorReadingVS(generics.ListAPIView):
   # queryset=sensorReading.objects.filter(readingDate__range=["2020-01-01", "2020-12-31"])
    queryset=sensorReading.objects.all()
    serializer_class= sensorReadingSer   
    filterset_class=sensorReadingFilter
    
                    