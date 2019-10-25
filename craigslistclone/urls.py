from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('', include('social_django.urls', namespace='social')),
    # path('logout/', logout, {'home': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    # path('register/',  views.register, name="register"),
    # path('login/',  views.login, name="login"),
    # path('logout/', views.logout, name="logout"),
    # path('home/', views.home, name="home")
]
