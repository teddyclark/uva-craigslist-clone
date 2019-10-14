from django.test import TestCase
from django.http import HttpRequest 
from django.test import SimpleTestCase

# Create your tests here.
class LoginTests(SimpleTestCase):
    #if the url works
    def test_login_to_home(self): 
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    #if the url doesn't work
    def test_login_to_home_broke(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'It did not work')
