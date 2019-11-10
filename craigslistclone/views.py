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
from django.contrib.auth.mixins import LoginRequiredMixin

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


class CreateListing(LoginRequiredMixin, CreateView):
    login_url = '/'
    template_name = 'createListing.html'
    form_class = ListingForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print("form valid")
        return super(CreateListing, self).form_valid(form)

""" This function just spits out all of the posts that have been made at the moment """
class ListingView(generic.ListView):
    login_url = '/'
    template_name = 'listings.html'
    form_class = ListingForm
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Listing.objects.all()