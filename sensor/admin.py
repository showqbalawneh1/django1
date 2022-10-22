from django.contrib import admin
from .models import pressureSensor,sensorReading

# Register your models here.


class pressureSensorAdmin(admin.ModelAdmin):
    fields=["labelSensor",
            "longitude",
            "latitude",
            ]
    
class sensorReadingAdmin(admin.ModelAdmin):
    fields=["sensor",
            "value",
            ]
    
admin.site.register(sensorReading , sensorReadingAdmin )
   
admin.site.register(pressureSensor ,pressureSensorAdmin )