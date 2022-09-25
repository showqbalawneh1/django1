from django.urls import path
from .views import pressureSensorVS,sensorReadingVS,reading_calc,reading_calc_f
from sensor import views
app_name= "sensor" 

urlpatterns=[
    path('/api/pressure_senors/',pressureSensorVS.as_view(),name="pressure_senors"),
    path('/api/pressure_readings/',sensorReadingVS.as_view(),name="pressure_readings"),
    path('/reading_calc_v/<str:since>/<str:until>/<str:calculation>',reading_calc.as_view(),name="sensorR"),
    path('/reading_calc_f/<str:since>/<str:until>/<str:calculation>',views.reading_calc_f,name="sensorR"),

   
]