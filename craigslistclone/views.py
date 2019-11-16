from django.urls import reverse_lazy
# from .utils import is_login
from .forms import ListingForm
from django.views.generic import CreateView
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
# from django.contrib import messages
from.models import User, Listing, GoogleUserList
from django.views import generic
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def createListing(request, template_name="createListing.html"):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if request.method == 'POST':
            form = ListingForm(request.POST)
            print("USERNAME: ", request.user.username)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.associated_username = user
                instance.save()
                return redirect('home')
        else:  
            form = ListingForm()
        return render(request, template_name, {'form': form})
    else:   
        return render(request, 'login.html')



class Profile(generic.ListView):
    login_url = '/'
    template_name = 'profile.html'
    model = Listing
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        user = User.objects.get(username=self.request.user.username)
        print("Username: ", user)
        return Listing.objects.all().filter(associated_username=user)

 

""" This function just spits out all of the posts that have been made at the moment """
class ListingView(generic.ListView):
    login_url = '/'
    template_name = 'listings.html'
    model = Listing
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Listing.objects.all()


def search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()
        if len(querystring) == 0:
            return redirect('/search/')

        results = Listing.objects.filter(Q(name__icontains=querystring) | Q(description__icontains=querystring))
        return render(request, 'results.html', {
            'querystring': querystring,
            'results': results,
        })

    else:
        return render(request, 'results.html')


def mark_sold(request):

    if request.user.is_authenticated:
        instance = Listing.objects.get(pk=request.id)

        user = request.user.username

        print("ID BITCH: ", instance)

        # return render(request, "createListing.html")
        return redirect("home.html")

    # user clicks button on post that says "mark sold"

    # BEFORE ANYTHING - request checks to make sure the post associated_username is equal to the logged in username - if not, throw error

    # request grabs ID of post instance

    # sends request to model to change the boolean value from False to True

    # redirects back to profile


    # return refresh page



def createListing(request, template_name="createListing.html"):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if request.method == 'POST':
            form = ListingForm(request.POST)
            print("USERNAME: ", request.user.username)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.associated_username = user
                instance.save()
                return redirect('home')
        else:  
            form = ListingForm()
        return render(request, template_name, {'form': form})
    else:   
        return render(request, 'login.html')