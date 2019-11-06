from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createListing/', views.CreateListing.as_view(), name="createListing"),
    path('', include('social_django.urls', namespace='social')),
    # path('logout/', logout, {'home': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    # path('register/',  views.register, name="register"),
    # path('login/',  views.login, name="login"),
    # path('logout/', views.logout, name="logout"),
    # path('home/', views.home, name="home")
    path('tempListing/', views.tempListing, name = 'tempListing'),
    path('welcome/', views.welcome, name = 'welcome'),
    path('profile/', views.profile, name='profile'),
    path('listings/', views.ListingView.as_view(), name='listings'),
]
