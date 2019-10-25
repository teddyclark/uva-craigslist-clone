# from django.urls import reverse_lazy
# from .utils import is_login
# from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.contrib import messages
from.models import User, GoogleUserList

from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect 

# def home(request):
#     if request.user.is_authenticated:
#         return render(request, 'home.html')
#     else:
#         return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated:

        if not GoogleUserList.objects.filter(registered_user=request.user.username).exists():
            return render(request, 'create_profile.html')
        else:
            return render(request, 'home.html')
    
    else:
        return render(request, 'login.html')


# def go_to_home(request):
#     return render(request, 'home.html')


# def request_page(request):
#     if(request.GET.get('mybtn')):
#         return render(request, 'home.html')



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
