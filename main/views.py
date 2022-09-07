from django.shortcuts import render
from datetime import datetime
import time
from .models import question ,choice
from django.http import HttpResponse
from django.db.models import F
from rest_framework import generics
from .serializers import qSerializer ,chSerializer
from django_filters import rest_framework as filters

# Create your views here.
def index(request,id):
    q=question.objects.get(id=id).pupDate
    t=question.objects.get(id=id)
    count=t.choice_set.count()
    choices=t.choice_set.all()
    t=question.objects.get(id=1)
    date=time.strptime("30 Nov 00", "%d %b %y")  
    return render(request, "main/index.html",{"date": date,"count":count,"question":t,"choices":choices})
class questionList (generics.ListCreateAPIView):
    queryset=question.objects.all()
    serializer_class=qSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields=('qText','pupDate')

    
class questionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=question.objects.all()
    serializer_class=qSerializer

class choiceList (generics.ListCreateAPIView):
    queryset=choice.objects.all()
    serializer_class=chSerializer
    
class choiceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=choice.objects.all()
    serializer_class=chSerializer
    
class qChoice(generics.ListCreateAPIView):
    queryset=choice.objects.all()
    serializer_class=chSerializer