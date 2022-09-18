from django.contrib import admin
from .models import tag

# Register your models here.

class tagAdmin(admin.ModelAdmin):
    fields=["label_tag",
            "content_type",
            "object_id",
            ]
admin.site.register(tag , tagAdmin )
   