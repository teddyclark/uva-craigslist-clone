from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url


from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('createListing/', views.CreateListing.as_view(), name="createListing"),
    path('createListing/', views.createListing, name="createListing"),
    path('', include('social_django.urls', namespace='social')),

    path('profile/', views.Profile.as_view(), name='profile'),
    path('listings/', views.ListingView.as_view(), name='listings'),
    path('logout/', views.logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
    path('<int:pk>/delete_post/', views.delete_post, name='delete_post'),
    path('<int:pk>/mark_sold/', views.mark_sold, name='mark_sold'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)