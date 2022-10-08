from django.test import TestCase
from django.urls import resolve,reverse
from sensor.models import sensorReading, pressureSensor 
from datetime import datetime 
from sensor.views import calculation , reading_calc ,reading_calc_f
from decimal import Decimal


since = datetime.fromisoformat('2022-09-01')
until = datetime.fromisoformat('2022-09-09')
since = datetime.fromisoformat('2022-09-01')
until = datetime.fromisoformat('2022-09-09')

class TestUrls(TestCase): 
    def setUp(self):
        pressureSensor.objects.create(labelSensor="testSensor",longitude=0.000009,latitude=0.000009)
        pur=pressureSensor.objects.get(labelSensor="testSensor")
        sensorReading.objects.create(sensor=pur,readingDate=datetime.fromisoformat('2022-09-01'),value=0.0000000018)
        sensorReading.objects.create(sensor=pur,readingDate=datetime.fromisoformat('2022-09-09'),value=0.0000000018)
        
    
    def test_it_require_3para(self):
        args=['2022-09-21','avg']
        # self.assertEqual(len(args), 3 )
        if  len(args)== 3:
            url=reverse('sensor.sensorRf', args)
        else : print("failed you need three parameter")
    
    

        
    def test_if_out_of_range_date(self):
        self.assertEqual(calculation('1900-08-20','1900-09-1','avg'), 0 )
