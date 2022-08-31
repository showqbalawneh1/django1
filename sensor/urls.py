from django.urls import path
from .views import pressureSensorVS,sensorReadingVS

app_name= "sensor" 

urlpatterns=[
    path('/api/pressure_senors/',pressureSensorVS.as_view(),name="pressure_senors"),
    path('/api/pressure_readings/',sensorReadingVS.as_view(),name="pressure_readings"),
    
    
]