from django.contrib import admin
from .models import question, choice

# Register your models here.


class choiceAdmin(admin.ModelAdmin):
    fields=["chText",
            "votes",
            "question"
            ]
    
class questionAdmin(admin.ModelAdmin):
    fields=["qText",
            "pupDate",
            ]
    
    
    
admin.site.register(question , questionAdmin )
   
admin.site.register(choice ,choiceAdmin )