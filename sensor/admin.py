from django.contrib import admin
from .models import pressureSensor,sensorReading

# Register your models here.
class sensorReadingInline (admin.TabularInline):
    model=sensorReading
    extra=1

class pressureSensorAdmin(admin.ModelAdmin):
    fields=["labelSensor",
            "longitude",
            "latitude",
            "serial_number"
            ]
    inlines=[sensorReadingInline,]
    readonly_fields = ["serial_number",]
    
class sensorReadingAdmin(admin.ModelAdmin):
    fields=["sensor",
            "value",
            "readingDate"
            ]
    readonly_fields = ["readingDate",]
    
admin.site.register(sensorReading , sensorReadingAdmin )
   
admin.site.register(pressureSensor ,pressureSensorAdmin )