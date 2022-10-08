from django.test import TestCase
from django.urls import resolve,reverse
from sensor.models import sensorReading, pressureSensor 
from datetime import datetime 
from sensor.views import calculation , reading_calc ,reading_calc_f
from decimal import Decimal
since = datetime.fromisoformat('2022-09-01')
until = datetime.fromisoformat('2022-09-09')

class TestViews(TestCase): 
    
    def setUp(self):
        pressureSensor.objects.create(labelSensor="testSensor",longitude=0.000009,latitude=0.000009)
        pur=pressureSensor.objects.get(labelSensor="testSensor")
        sensorReading.objects.create(sensor=pur,readingDate=datetime.fromisoformat('2022-09-01'),value=0.0000000018)
        sensorReading.objects.create(sensor=pur,readingDate=datetime.fromisoformat('2022-09-09'),value=0.0000000018)
        
        
    def test_sum_correct(self):
         value =calculation(since, until,'sum')
         self.assertEqual(value,Decimal('3.6e-9' ))
     
        
    def test_avg_correct(self):
        value =calculation(since, until,'avg')
        self.assertEqual(value,Decimal('1.8e-9' ))
        
    def test_until_after_since_para(self):
        self.assertEqual(calculation('2022-09-9','2022-09-1','avg'), 0 )
        
    def test_retrive_value(self):
        pr = pressureSensor.objects.get(labelSensor="testSensor")
        value =calculation(since, until,'sum')
        self.assertEqual( type(value),Decimal)
        
    
         # response = c.get('/flowLess/reading_calc_f/2022-09-01/2022-09-09/avg')
        # {'since': '2022-09-01', 'until': '2022-09-09','calculation':'sum'}
        # print("hi hi")
        # content= response.content
        # soup = BeautifulSoup(content, 'content.parser')
        # for item in soup.find_all('h3'): print(item)