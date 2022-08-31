from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class question(models.Model):
    qText= models.CharField(max_length=200)
    pupDate= models.DateTimeField('date published',default=datetime.now)
    
    def __str__(self):
        return self.qText
    
    def publishedRecently(self):
        return self.pupDate.month >=datetime.now().month
    
    
class choice (models.Model):
    chText=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    question= models.ForeignKey(question, on_delete=models.CASCADE)
    def __str__(self):
        return self.chText
    
