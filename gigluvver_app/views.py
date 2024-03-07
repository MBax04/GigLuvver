from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse

from gigluvver_app.forms import UserForm, ArtistProfileForm

def home(request):
    return HttpResponse("The Home page works <a href='/gigluvver_app/log_in/'>About</a>")


def log_in(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('gigluvver_app:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return HttpResponse("The log_in page works")

def my_tickets(request):
    return HttpResponse("The my_tickets page works")

def user_profile(request):
    return HttpResponse("The user_profile page works")

def create_account(request):
    return HttpResponse("The create_account page works")

def create_user_account(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return HttpResponse("The create_user_account page works")
    #render(request,
        # 'gigluvver_app/login-createaccount.html',
        # context = {'user_form': user_form,
        # 'registered': registered})

def create_artist_account(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ArtistProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.isArtist = True

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ArtistProfileForm()

    #return render(request,
    #              'gigluvver_app/artistLogin-createAccount.html',
    #              context = {'user_form': user_form,
    #                         'profile_form': profile_form,
    #                         'registered': registered})
    return HttpResponse("The create_artist_account page works")

def artist_log_in(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('gigluvver_app:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return HttpResponse("The artist_log_in page works")


def my_gigs(request):
    return HttpResponse("The my_gigs page works")

def artist_profile(request):
    return HttpResponse("The artist_profile page works")

def gigs(request):
    return HttpResponse("The gigs page works")

def gig(request):
    return HttpResponse("The gig page works")

def map(request):
    return HttpResponse("The map page works")

