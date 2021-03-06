import unittest

from django.test import TestCase, Client
from django.urls import reverse, resolve
from craigslistclone.models import Listing
from craigslistclone.views import home
from users.models import CustomUser

class TestUrl(unittest.TestCase):
    # tests root url resolves to home
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
class TestUserModel(unittest.TestCase):
    def test_usernameTest(self):
        user = CustomUser(username = 'tester')
        self.assertEqual(user.username, "tester")
    def test_first_name(self):
        user = CustomUser(first_name = "John")
        self.assertEqual(user.first_name, "John")
    # exception test
    def test_last_name(self):
        user = CustomUser(last_name = "Doe")
        self.assertFalse(user.last_name == "Day")

class ViewsTestNoUser(unittest.TestCase):
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
    def testCreatePostPage(self):                  
       response = self.client.get("/createListing/")
       self.assertEqual(response.status_code, 200)
    # def testListingsPage(self):                 
    #    response = self.client.get("/listings/")
    #    self.assertEqual(response.status_code, 302)
    

# # tests features about listings 
class TestListing(unittest.TestCase):
    def test_listingname(self):
        listing = Listing(title = 'testname')
        self.assertEqual(listing.title, "testname")
    def test_price(self):
        listing = Listing(title = 'testname', price = 51.12)
        self.assertEqual(listing.price, 51.12)
    def test_bad_condition(self):
        listing = Listing(title = 'testname', price = 51.12, condition = 0)
        self.assertEqual(listing.condition, 0)
    def test_good_condition(self):
        listing = Listing(title = 'testname', price = 51.12, condition = 3)
        self.assertEqual(listing.condition, 3)
    def test_description(self):
        listing = Listing(title = 'testname', price = 51.12, condition = 0, description = 'great product')
        self.assertEqual(listing.description, 'great product')
    def test_sold(self):
        listing = Listing(title = 'testname', price = 51.12, condition = 0, description = 'great product', sold = True)
        self.assertEqual(listing.sold, True)
    def test_not_sold(self):
        listing = Listing(title = 'testname', price = 51.12, condition = 0, description = 'great product', sold = False)
        self.assertEqual(listing.sold, False)
    def test_cateogry_textbook(self):
        listing = Listing(title = 'testname', price = 51.12, condition = 0, description = 'great product', sold = False, category = 'TB')
        self.assertEqual(listing.category, 'TB')
    def test_cateogry_default(self):
        listing = Listing(title = 'testname', price = 51.12, condition = 0, description = 'great product', sold = False, category = 'OT')
        self.assertEqual(listing.category, 'OT')

class TestListing_restriction(unittest.TestCase):
    # test name that is too long
    def test_listingname2(self):
        listing = Listing(title = 'item' * 40)
        b = listing.title == 'item'
        self.assertEqual(b, False)
    # test price that is not a number
    def test_price_wrong(self):
        listing = Listing(title = 'testname', price = 'happy')
        b = listing.price == 0
        self.assertEqual(b, False)

class ViewsTest_login(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser')
        login = self.client.login(username='testuser')
    def testLogInPage(self):
       response = self.client.get("/")
       self.assertEqual(response.status_code, 200)


# class TestStringMethods(unittest.TestCase):
#     # temporary tests
#     def test_1(self):
#         a = 1
#         self.assertEqual(1, a)
#     def test_2(self):
#         b = 4
#         a = 1
#         self.assertFalse(a == b)
