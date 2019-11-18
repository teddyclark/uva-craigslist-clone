from django.urls import reverse_lazy
# from .utils import is_login
from .forms import ListingForm
from django.views.generic import CreateView
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
# from django.contrib import messages
from.models import Listing, GoogleUserList
from django.views import generic
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from users.models import CustomUser

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')

#def profile(request):
#    if request.user.is_authenticated:
#        return render(request, 'profile.html')
#    else:
#        return render(request, 'login.html')
class Profile(generic.ListView):
    login_url = '/'
    template_name = 'profile.html'
    model = Listing
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        user = CustomUser.objects.get(username=self.request.user.username)
        print("Username: ", user)
        return Listing.objects.all().filter(associated_username=user)



def logout(request):
    auth_logout(request)
    return redirect('/')

# def createListingPage(request):
#     if request.user.is_authenticated:
#         return render(request, 'createListing.html')
#     else:
#         return render(request, 'login.html')

# class CreateListing(LoginRequiredMixin, CreateView):
#    login_url = '/'
#    template_name = 'createListing.html'
#    form_class = ListingForm
#    success_url = reverse_lazy('listings')

#    def form_valid(self, form):
#        print("form valid")
#        return super(CreateListing, self).form_valid(form)

 
def createListing(request, template_name="createListing.html"):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(username=request.user.username)
        if request.method == 'POST':
            form = ListingForm(request.POST, request.FILES)
            print("USERNAME: ", request.user.username)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.associated_username = user
                print("IMAGE FIELD: ", instance.image)
                instance.save()
                return redirect('listings')
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


def delete_post(request, id=None):

    creator = request.user.username
    # instance = get_object_or_404(Listing, id=id)

    print("CREATOR: ", creator)

    return render(request, 'delete_post.html')

    # print("INSTANCE: ", instance)

    # if request.method == "POST" and request.user.is_authenticated and request.user.username == creator:

    #     instance.delete()

    #     return render(request, 'delete_post.html')

    # else:
    #     return render(request, 'createListing.html')

# def delete_post(request):
#     return render(request, 'delete_post.html')



# def movies_delete_view(request, id=None):

#     movie= get_object_or_404(Movie, id=id)

#     creator= movie.user.username

#     if request.method == "POST" and request.user.is_authenticated and request.user.username == creator:
#         movie.delete()
#         messages.success(request, "Post successfully deleted!")
#         return HttpResponseRedirect("/Blog/list/")
    
#     context= {'movie': movie,
#               'creator': creator,
#               }
    
#     return render(request, 'Blog/movies-delete-view.html', context)
