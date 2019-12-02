from django.urls import reverse_lazy
from .forms import ListingForm
from django.views.generic import CreateView
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from.models import Listing, GoogleUserList
from django.views import generic
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from users.models import CustomUser
from django.utils import timezone
from geopy import geocoders

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')


class Profile(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    template_name = 'profile.html'
    model = Listing
    # context_object_name = 'latest_post_list'

    # def get_queryset(self):
    #     user = CustomUser.objects.get(username=self.request.user.username)
    #     print("Username: ", user)
    #     return Listing.objects.filter(associated_username=user)
    
    def get_context_data(self, **kwargs):
        user = CustomUser.objects.get(username=self.request.user.username)
        obj = super(Profile, self).get_context_data(**kwargs)
        obj['active_listings'] = Listing.objects.filter(sold=False, associated_username=user)
        obj['inactive_listings'] = Listing.objects.filter(sold=True, associated_username=user)
        return obj



def logout(request):
    auth_logout(request)
    return redirect('/')

 
def createListing(request, template_name="createListing.html"):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(username=request.user.username)
        if request.method == 'POST':
            form = ListingForm(request.POST, request.FILES)
            print("USERNAME: ", request.user.username)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.associated_username = user

                # it is necessary to initialize values for latitude and longitude to avoid potential errors - these point to Rice Hall
                instance.latitude = 38.031603
                instance.longitude = -78.510779
                print("LATITUDE: ", instance.latitude, ", LONGITUDE: ", instance.longitude)
                print("IMAGE FIELD: ", instance.image)


                """ This following code takes in pickup_location from the model,
                    converts that location into coordinates, and saves it the
                    appropriate fields in the model
                """

                # addr = instance.pickup_location
                # g = geocoders.GoogleV3(api_key='AIzaSyBZiiJxIQrpxmMopu-UyqmZEYX7np2CKsw')
                # location = g.geocode(addr, timeout=10)

                # instance.latitude = location.latitude
                # instance.longitude = location.longitude

                # print("LATITUDE: ", instance.latitude, ", LONGITUDE: ", instance.longitude)

                instance.save()
                return redirect('listings')
        else:
            form = ListingForm()
        return render(request, template_name, {'form': form})
    else:
        return render(request, 'login.html')


class ListingView(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    template_name = 'listings.html'
    model = Listing
    #form_class = ListingForm
    context_object_name = 'latest_post_list'
    paginate_by = 10

    def get_queryset(self):
        querystring = self.request.GET.get('q')
        categorystring = self.request.GET.get('cat')
        switcher = {
            "All": "All",
            "Textbook": "TB",
            "Furniture": "FN", 
            "Clothes": "CL",
            "Electronics": "EL",
            "Other": "OT",   
        }
        category = switcher.get(categorystring, "trolol")
        if querystring:
            return Listing.objects.filter(Q(sold=False) & (Q(title__icontains=querystring) | Q(description__icontains=querystring)))
        if category:
            if category == "All":
                return Listing.objects.filter(sold=False)
            return Listing.objects.filter(Q(sold=False) & Q(category__icontains=category))
        else:
            return Listing.objects.filter(sold=False)


def search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()
        if len(querystring) == 0:
            return redirect('/search/')

        results = Listing.objects.filter(Q(sold=False) & (Q(title__icontains=querystring) | Q(description__icontains=querystring)))
        return render(request, 'results.html', {
            'querystring': querystring,
            'results': results,
        })

    else:
        return render(request, 'results.html')


def mark_unsold(request, pk):
    instance = get_object_or_404(Listing, pk=pk)
    instance.sold = False
    instance.save()
    return HttpResponseRedirect(reverse('profile'))

def mark_sold(request, pk):
    instance = get_object_or_404(Listing, pk=pk)
    instance.sold = True
    instance.save()
    return HttpResponseRedirect(reverse('profile'))


def delete_post(request, pk):
    instance = get_object_or_404(Listing, pk=pk)
    instance.delete()
    return HttpResponseRedirect(reverse('profile'))


class DetailView(generic.DetailView):
    model = Listing
    template_name = 'listing_details.html'

    def get_queryset(self):
        return Listing.objects.all()
