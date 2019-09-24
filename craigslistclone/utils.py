from django.core.exceptions import PermissionDenied
from django.core import serializers
from .models import User


def is_login(func):
    def verify(request, *args, **kwargs):
        if 'user' in request.session and User.objects.get(id=request.session['user']):
            return func(request, *args, **kwargs)
        else:
            print(request.session.session_key)
            raise PermissionDenied
    return verify
