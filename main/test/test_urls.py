from django.test import SimpleTestCase
from django.urls import reverse ,resolve 
import main
class TestUrls(SimpleTestCase): 
    
    def test_list_url_is_resolved (self):
        url=reverse('main.qList')
        self.assertEquals( resolve(url).func.view_class  , main.views.questionList)
        #self.assertEquals( resolve(url)._func_path , 'main.views.questionList')
        