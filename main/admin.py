from django.contrib import admin
from .models import question, choice
from tags.models import tag
from django.contrib.contenttypes import admin as adm

# Register your models here.

class choiceInline (admin.TabularInline):
    model = choice
    max_num = 10
    extra = 1

class tagInline (adm.GenericTabularInline):
    model=tag
    extra=1
    
    
class choiceAdmin(admin.ModelAdmin):
    fields=["chText",
            "votes",
            "question",
            ]
    inlines = [tagInline]
class questionAdmin(admin.ModelAdmin):
    fields=["qText",
            "pupDate",
            ]
    inlines = [
        choiceInline,tagInline
    ]
    
    
    
admin.site.register(question , questionAdmin )
   
admin.site.register(choice ,choiceAdmin )