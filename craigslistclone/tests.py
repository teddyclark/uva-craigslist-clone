import unittest

from django.test import TestCase, Client
from django.urls import reverse, resolve
from craigslistclone.models import User, Listing
from craigslistclone.views import home

class TestStringMethods(unittest.TestCase):
    # temporary tests
    def test_1(self):
        a = 1
        self.assertEqual(1, a)
    def test_2(self):
        b = 4
        a = 1
        self.assertFalse(a == b)

class TestUrl(unittest.TestCase):
    # tests root url resolves to home
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
class TestUserModel(unittest.TestCase):
    def test_usernameTest(self):
        user = User(username = 'tester')
        self.assertEqual(user.username, "tester")
    def test_first_name(self):
        user = User(firstName = "John")
        self.assertEqual(user.firstName, "John")
    # exception test
    def test_last_name(self):
        user = User(lastName = "Doe")
        self.assertFalse(user.lastName == "Day")  

class ViewsTestNoUser(TestCase):
    def setUp(self):
        self.client = Client()
        #testing with no user login
    def testLogInPage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def testHomePage(self):
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 404)
    def testProfilePage(self):
        response = self.client.get("profile/")
        self.assertEqual(response.status_code, 404)
    #def testCreatePostPage(self):                  #this is a bug
    #    response = self.client.get("/createListing/")
    #    self.assertEqual(response.status_code, 404)
    #def testListingsPage(self):
    #    response = self.client.get("/listings/")
    #    self.assertEqual(response.status_code, 404)
'''
class ViewsTest(TestCase):
    def setUp(self):
        #user = GoogleUserList(registered_user = "john")
        self.client = Client()
        #self.client.force_login(user)
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
    #def testLogInPage(self):
    #    response = self.client.get("/")
    #    self.assertEqual(response.status_code, 200)
'''

class TestListing(unittest.TestCase):
    def test_listingname(self):
        listing = Listing(name = 'testname')
        self.assertEqual(listing.name, "testname")
    def test_price(self):
        listing = Listing(name = 'testname', price = 51.12)
        self.assertEqual(listing.price, 51.12)


    
