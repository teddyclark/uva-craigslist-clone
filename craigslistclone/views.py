from django.urls import reverse_lazy
# from .utils import is_login
from .forms import ListingForm
from django.views.generic import CreateView
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.contrib import messages
from.models import User, Listing


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')


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


# def newUser(self, request):
#     if GoogleUserList.objects.filter(registered_user__startswith='bc6cd'):
#         return HttpResponse("high five")
#     else:
#         return HttpResponse("rip")


# def index(request):
#     if 'user' in request.session:
#         return redirect(reverse('home'))
#     else:
#         return render(request, 'index.html')


# def login(request):
#     if request.method == 'POST':
#         login = User.objects.login(request.POST.copy())
#         if isinstance(login, list):
#             for item in login:
#                 messages.error(request, item)
#             return redirect(reverse('index'))
#         else:
#             request.session['user'] = login
#             return redirect(reverse('home'))
#     else:
#         return redirect(reverse('index'))


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if not form.is_valid():
#             return render(request, 'register.html', {'form': RegisterForm})
#         else:
#             register = User.objects.register(form.cleaned_data)
#             request.session['user'] = register
#             return redirect(reverse('home'))

#     else:
#         return render(request, 'register.html', {'form': RegisterForm})


# def logout(request):
#     request.session.pop('user')
#     return redirect(reverse('index'))


# @is_login
# def home(request):
#     return render(request, 'home.html')
