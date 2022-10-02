from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

from rest_framework import generics
from .models import pressureSensor,sensorReading
from .serializers import pressureSensorSer, sensorReadingSer
from datetime import datetime 
from django_filters import rest_framework as filters
from django.http import HttpResponse
###
#from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Sum,Avg
import datetime

    # returns {'value__sum': (800)} for 
class reading_calc(APIView):
    def get(self, request , *args , **kwargs ):
        since = datetime.datetime.fromisoformat(kwargs['since'])
        until = datetime.datetime.fromisoformat(kwargs['until'])
        calc= kwargs['calculation']
        return Response(calculation(since,until,calc))
        
        
def calculation (since,until,calc):
        q=sensorReading.objects.filter(readingDate__range=[since, until])
        if q.exists() == 0 :
            return 0
        if calc == 'sum':
            value= q.aggregate(Sum('value'))
            return value['value__sum']
        elif calc == 'avg':
            value = q.aggregate(Avg('value'))
            return value['value__avg']
        else :
            return 'choose avg or sum '
    
def reading_calc_f(request, *args , **kwargs ):
        if (kwargs['since']>=kwargs['until']):
            val=0
            messages="since > until "
            return render(request,"main/sensorR.html",{"operation": operation ,"value":val, message:"message"})
        
        since = datetime.datetime.fromisoformat(kwargs['since'])
        until = datetime.datetime.fromisoformat(kwargs['until'])
        q=sensorReading.objects.filter(readingDate__range=[since, until])
        operation= kwargs['calculation']
        if operation == 'sum':
            value= q.aggregate(Sum('value'))
            val=value['value__sum']
        elif operation == 'avg':
            value = q.aggregate(Avg('value'))
            val=value['value__avg']
        else :
            val=0
     
        return render(request,"main/sensorR.html",{"operation": operation ,"value":val})
    
  

class pressureSensorFilter(filters.FilterSet):
    class Meta:
        model=pressureSensor
        fields={
            'labelSensor':['icontains'],
            'installationDate':['lte']
        }
class pressureSensorVS(generics.ListCreateAPIView):
    queryset=pressureSensor.objects.all()
    serializer_class=pressureSensorSer
    filterset_class=pressureSensorFilter
    
class sensorReadingFilter(filters.FilterSet):
    name = filters.NumberFilter(field_name="value", lookup_expr='lte')
    name = filters.DateTimeFilter(field_name="readingDate", input_formats=['%Y-%m-%d','%d-%m-%Y'],lookup_expr='icontains')
    class Meta:
        model=sensorReading
        fields=('sensor','readingDate')
class sensorReadingVS(generics.ListCreateAPIView):
   # queryset=sensorReading.objects.filter(readingDate__range=["2020-01-01", "2020-12-31"])
    queryset=sensorReading.objects.all()
    serializer_class= sensorReadingSer   
    filterset_class=sensorReadingFilter
    

def welcome ():
    return HttpResponse("hi hi")
                    