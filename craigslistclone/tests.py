from django.test import TestCase
from django.http import HttpRequest 
from django.test import SimpleTestCase

# Create your tests here.
class LoginTests(SimpleTestCase):
    #tests to see if it gets to the login page
    def test_login_to_home(self): 
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    

