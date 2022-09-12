from django.contrib import admin
from .models import question, choice

# Register your models here.

class choiceInline (admin.TabularInline):
    model = choice
    max_num = 10
    extra = 1


class choiceAdmin(admin.ModelAdmin):
    fields=["chText",
            "votes",
            "question"
            ]
class questionAdmin(admin.ModelAdmin):
    fields=["qText",
            "pupDate",
            ]
    inlines = [
        choiceInline,
    ]
    
    
    
admin.site.register(question , questionAdmin )
   
admin.site.register(choice ,choiceAdmin )