from django.urls import reverse_lazy
# from .utils import is_login
from .forms import ListingForm
from django.views.generic import CreateView
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.contrib import messages
from.models import User, Listing, GoogleUserList
from django.views import generic
from django.contrib.auth import logout as auth_logout

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')


class CreateListing(CreateView):
    template_name = 'createListing.html'
    form_class = ListingForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print("form valid")
        # need to define Key to User 
        #creator = User.objects.get(id=self.request.session['user'])
        # for now no user
        #form.instance.creator = creator
        return super(CreateListing, self).form_valid(form)

""" This function just spits out all of the posts that have been made at the moment """
class ListingView(generic.ListView):
    template_name = 'listings.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Listing.objects.all()