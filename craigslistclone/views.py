#from django.urls import reverse_lazy
#from .utils import is_login
#from .forms import RegisterForm, ListingForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
#from django.contrib import messages
from .models import User, Listing
from .forms import ListingForm
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden

# User login/logout

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, "home.html")
'''
def index(request):
    if 'user' in request.session:
        return redirect(reverse('home'))
    else:
        return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        login = User.objects.login(request.POST.copy())
        if isinstance(login, list):
            for item in login:
                messages.error(request, item)
            return redirect(reverse('index'))
        else:
            request.session['user'] = login
            return redirect(reverse('home'))
    else:
        return redirect(reverse('index'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'register.html', {'form': RegisterForm})
        else:
            register = User.objects.register(form.cleaned_data)
            request.session['user'] = register
            return redirect(reverse('home'))

    else:
        return render(request, 'register.html', {'form': RegisterForm})


def logout(request):
    request.session.pop('user')
    return redirect(reverse('index'))


@is_login
def home(request):
    return render(request, 'home.html')
'''

class ListingView(generic.ListView):
    model = Listing
    template_name = 'listings.html'

    def get_queryset(self):
        return Listing.objects.filter(pub_date__lte=timezone.now())
# User upload images

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html')

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {
        'listings' : listings
    })

def upload_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Hello")
    else:
        form = ListingForm()
    return render(request, 'upload_listing.html', {
        'form': form
    })

