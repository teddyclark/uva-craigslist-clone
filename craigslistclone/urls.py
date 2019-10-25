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
    #path('listings/', views.listings, name="listings"),
    path('', views.ListingView.as_view(), name='listings'),
    path('listings/upload', views.upload_listing, name="upload_image"),
    path('home/', views.home, name="home")
]
