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



# class UserManager(models.Manager):
#     def register(self, userData):
#         messages = []

#         for field in userData:

#             if len(userData[field]) == 0:
#                 fields = {
#                     'firstName': 'FirstName',
#                     'lastName': 'LastName',
#                     'username': 'UserName',
#                     'password': 'Password',
#                     'confirmPassword': 'Confirmation Password',
#                 }
#                 messages.append(fields[field]+' must be filled in')

#         try:
#             User.objects.get(username=userData['username'])
#             messages.append('Username already registered')
#         except:
#             pass

#         if len(messages) > 0:
#             print("returning messages")
#             return messages
#         else:
#             hashed_pw = bcrypt.hashpw(
#                 userData['password'].encode(), bcrypt.gensalt())
#             new_user = User.objects.create(
#                 firstName=userData['firstName'], lastName=userData['lastName'], username=userData['username'], hashed_pw=hashed_pw)
#             return new_user.id

#     def login(self, userData):
#         messages = []
#         for field in userData:
#             if len(userData[field]) == 0:
#                 fields = {
#                     'login_username': 'Username',
#                     'login_password': 'Password'
#                 }
#                 messages.append(fields[field]+' must be filled in')

#         try:
#             user = User.objects.get(username=userData['login_username'])
#             if bcrypt.checkpw(userData['login_password'].encode(), user.hashed_pw):
#                 return user.id
#             else:
#                 messages.append('Wrong password')
#         except:
#             messages.append('User not registered')

#         if len(messages) > 0:
#             return messages


# class User(models.Model):
#     firstName = models.CharField(max_length=50)
#     lastName = models.CharField(max_length=50)
#     username = models.CharField(max_length=50, unique=True)
#     hashed_pw = models.BinaryField(max_length=255)
#     objects = UserManager()


# this model represents a list of users who have accounts with our site
class GoogleUserList(models.Model):
    registered_user = models.CharField(max_length=30)

    def __str__(self):
        return self.registered_user


class ListingManager(models.Manager):

    def placeholder(self, user_id):
        user = User.objects.get(id=user_id)


class Listing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    image = models.ImageField(null=True, blank=True, upload_to='image_folder/')
    associated_username = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    sold = models.BooleanField(default=False)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    #cover = Image.open(image)
    #if cover not in ("L", "RGB"):
        #cover = cover.convert("RGB")

    #cover = cover.thumbnail((500, 500), Image.ANTIALIAS)
    #cover.save()

    price = models.DecimalField(
        max_digits = 6, 
        decimal_places = 2,
        validators=[MinValueValidator(Decimal('0.01'))],
        default = 0.00
    )
    condition = models.CharField(
        max_length = 1,
        choices = (
            ('0', 'Bad'),
            ('1', 'Poor'),
            ('2', 'Decent'),
            ('3', 'Good'),
            ('4', 'New'),
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
    
    place = models.CharField(
        max_length = 1,
        choices = (
            ('0', 'Rotunda'),
            ('1', 'Rice Hall'),
            ('2', 'O-Hill'),
            ('3', '1515 on the Corner'),
            ('4', 'McLeod Hall'),
        ),
        default = '0'
    )
    

    # need to figure out the key for User before we can implement creator
    #creator = models.ForeignKey(User, on_delete=models.PROTECT) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ListingManager()
