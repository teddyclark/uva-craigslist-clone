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

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

# def createListingPage(request):
#     if request.user.is_authenticated:
#         return render(request, 'createListing.html')
#     else:
#         return render(request, 'login.html')

#class CreateListing(LoginRequiredMixin, CreateView):
#    login_url = '/'
#    template_name = 'createListing.html'
#    form_class = ListingForm

#    # form_class = ListingForm
#    success_url = reverse_lazy('home')

#    def form_valid(self, form):
#        print("form valid")
#        return super(CreateListing, self).form_valid(form)




def createListing(request, template_name="createListing.html"):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        # staffprofile.user = user
        print(" FUCKKKKKKKK", user)
        if request.method == 'POST':
            form = ListingForm(request.POST)
            print("USERNAME: ", request.user.username)
            if form.is_valid():
                instance = form.save(commit=False)
                # Listing.associated_username = request.user.username
                instance.associated_username = user
                instance.save()
                return redirect('home')
        else:
            form = ListingForm()
        return render(request, template_name, {'form': form})
    else:
        return render(request, 'login.html')
        
""" This function just spits out all of the posts that have been made at the moment """
class ListingView(generic.ListView):
    login_url = '/'
    template_name = 'listings.html'
    model = Listing
    #form_class = ListingForm
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