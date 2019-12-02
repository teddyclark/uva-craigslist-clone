from django.db import models
#from PIL import Image, ImageOps
#rom io import StringIO
import bcrypt
from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import uuid
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils import timezone
import datetime


# this model represents a list of users who have accounts with our site
class GoogleUserList(models.Model):
    registered_user = models.CharField(max_length=30)

    def __str__(self):
        return self.registered_user


class ListingManager(models.Manager):

    def placeholder(self, user_id):
        user = User.objects.get(id=user_id)


class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    image = models.ImageField(null=True, blank=True, upload_to='image_folder/')
    associated_username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    sold = models.BooleanField(default=False)
    pickup_location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    price = models.DecimalField(
        max_digits = 6, 
        decimal_places = 2,
        validators=[MinValueValidator(Decimal('0.01'))],
        default = 0.00
    )
    condition = models.CharField(
        max_length = 1,
        choices = (
            ('0', 'New'),
            ('1', 'Good'),
            ('2', 'Decent'),
            ('3', 'Poor'),
        ),
        default = '2'
    )
    category = models.CharField(
        max_length = 2,
        choices = (
            ('TB', 'Textbook'),
            ('FN', 'Furniture'),
            ('CL', 'Clothes'),
            ('EL', 'Electronics'),
            ('OT', 'Other'),
        ),
        default = 'OT'
    )
    
    # place = models.CharField(
    #     max_length = 1,
    #     choices = (
    #         ('0', 'Rotunda'),
    #         ('1', 'Rice Hall'),
    #         ('2', 'O-Hill'),
    #         ('3', '1515 on the Corner'),
    #         ('4', 'McLeod Hall'),
    #     ),
    #     default = '0'
    # )
    

    # need to figure out the key for User before we can implement creator
    #creator = models.ForeignKey(User, on_delete=models.PROTECT) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ListingManager()
