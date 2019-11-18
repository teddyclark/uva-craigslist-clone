import unittest

from django.test import TestCase, Client
from django.urls import reverse, resolve
from craigslistclone.models import User, Listing
from craigslistclone.views import home
from django.utils import timezone
from django.db import models

class TestStringMethods(unittest.TestCase):
    # temporary tests
    def test_1(self):
        a = 1
        self.assertEqual(1, a)
    def test_2(self):
        b = 4
        a = 1
        self.assertFalse(a == b)

# tests root url resolves to home
class TestUrl(unittest.TestCase):
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

# tests user model to make sure fields are correct 
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

# tests access when not logged in
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
    def testCreatePostPage(self):                  #this is a bug
       response = self.client.get("/createListing/")
       self.assertEqual(response.status_code, 302)


class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        login = self.client.login(username='testuser')
        # user = GoogleUserList(registered_user = "john")
        # self.client = Client()
        # # self.client.force_login(user)
        # self.client.force_login(User.objects.get_or_create(username='testuser')[0])
    def testLogInPage(self):
       response = self.client.get("/")
       self.assertEqual(response.status_code, 200)

# tests features about the listing
class TestListing(unittest.TestCase):
    def test_listingname(self):
        listing = Listing(name = 'testname')
        self.assertEqual(listing.name, "testname")
    def test_price(self):
        listing = Listing(name = 'testname', price = 51.12)
        self.assertEqual(listing.price, 51.12)

class TestListingTime(unittest.TestCase):
    def test_upload_time(self):
        listing = Listing(created_at = timezone.now())
        self.assertIs(listing.created_at, listing.created_at)
    # def test_listingname(self):
    #     listing = Listing(created_at = 'testname')
    #     self.assertEqual(listing.name, "testname")
    # def test_price(self):
    #     listing = Listing(name = 'testname', price = 51.12)
    #     self.assertEqual(listing.price, 51.12)
