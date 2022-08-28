from django.shortcuts import render
from datetime import datetime
import time
from .models import question ,choice
from django.http import HttpResponse
from django.db.models import F

# Create your views here.
def index(request,id):
    q=question.objects.get(id=id).pupDate
    t=question.objects.get(id=id)
    count=t.choice_set.count()
    choices=t.choice_set.all()
    t=question.objects.get(id=1)
    date=time.strptime("30 Nov 00", "%d %b %y")  
    return render(request, "main/index.html",{"date": date,"count":count,"question":t,"choices":choices})
