from django.urls import path
from .views import pressureSensorVS,sensorReadingVS
from sensor import views
app_name= "sensor" 

urlpatterns=[
    path('/api/pressure_senors/',pressureSensorVS.as_view(),name="pressure_senors"),
    path('/api/pressure_readings/',sensorReadingVS.as_view(),name="pressure_readings"),

    
    
    
]