from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=15)
    
class Post(models.Model):
    content = models.TextField()
    author = models.ManyToManyField(Author)
    
