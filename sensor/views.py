from rest_framework import generics
from .models import pressureSensor,sensorReading
from .serializers import pressureSensorSer, sensorReadingSer
from datetime import datetime 
from django_filters import rest_framework as filters


class pressureSensorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model=pressureSensor
        fields=('labelSensor','installationDate')
class pressureSensorVS(generics.ListAPIView):
    queryset=pressureSensor.objects.all()
    serializer_class=pressureSensorSer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class=pressureSensorFilter
    
class sensorReadingFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model=sensorReading
        fields=('value','readingDate')
class sensorReadingVS(generics.ListAPIView):
    queryset=sensorReading.objects.filter(readingDate__range=["2020-01-01", "2020-12-31"])
    serializer_class= sensorReadingSer   
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class=sensorReadingFilter
    
                    