from django.db import models
import bcrypt


class UserManager(models.Manager):
    def register(self, userData):
        messages = []

        for field in userData:

            if len(userData[field]) == 0:
                fields = {
                    'firstName': 'FirstName',
                    'lastName': 'LastName',
                    'username': 'UserName',
                    'password': 'Password',
                    'confirmPassword': 'Confirmation Password',
                }
                messages.append(fields[field]+' must be filled in')

        try:
            User.objects.get(username=userData['username'])
            messages.append('Username already registered')
        except:
            pass

        if len(messages) > 0:
            print("returning messages")
            return messages
        else:
            hashed_pw = bcrypt.hashpw(
                userData['password'].encode(), bcrypt.gensalt())
            new_user = User.objects.create(
                firstName=userData['firstName'], lastName=userData['lastName'], username=userData['username'], hashed_pw=hashed_pw)
            return new_user.id

    def login(self, userData):
        messages = []
        for field in userData:
            if len(userData[field]) == 0:
                fields = {
                    'login_username': 'Username',
                    'login_password': 'Password'
                }
                messages.append(fields[field]+' must be filled in')

        try:
            user = User.objects.get(username=userData['login_username'])
            if bcrypt.checkpw(userData['login_password'].encode(), user.hashed_pw):
                return user.id
            else:
                messages.append('Wrong password')
        except:
            messages.append('User not registered')

        if len(messages) > 0:
            return messages


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    hashed_pw = models.BinaryField(max_length=255)
    objects = UserManager()

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='listings/images/')

    def __str__(self):
        return self.title
