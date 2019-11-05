# from django.urls import reverse_lazy
# from .utils import is_login
# from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.contrib import messages
from.models import GoogleUserList

from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect 

# def home(request):
#     if request.user.is_authenticated:
#         return render(request, 'home.html')
#     else:
#         return render(request, 'login.html')


# def home(request):
#     if request.user.is_authenticated:

#         if not GoogleUserList.objects.filter(registered_user=request.user.username).exists():
#             return render(request, 'create_profile.html')
#         else:
#             return render(request, 'home.html')
    
#     else:
#         return render(request, 'login.html')



def home(request):
    if request.user.is_authenticated:
        if not GoogleUserList.objects.filter(registered_user=request.user.username).exists():
            new_user = GoogleUserList(registered_user=request.user.username)
            new_user.save()
        return render(request, 'home.html')

    else:
        return render(request, 'login.html')



# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


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
