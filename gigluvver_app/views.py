from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from gigluvver_app.forms import UserForm, ArtistProfileForm

def home(request):
    response = render(request, 'home.html')
    return response

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
        response = render(request, 'user_login.html')
        return response

def my_tickets(request):
    response = render(request, 'tickets.html')
    return response

def user_profile(request):
    response = render(request, 'account.html')
    return response

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

    response = render(request, 'create_user_account.html',
                      context = {'user_form': user_form, 'registered': registered})
    return response

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
            profile.is_artist = True

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ArtistProfileForm()
        
    response = render(request, 'create_artist_account.html',
                      context = {'user_form': user_form,
                                 'profile_form': profile_form,
                                 'registered': registered})
    return response

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
        response = render(request, 'artist_login.html')
        return response

def my_gigs(request):
    response = render(request, 'my_gigs.html')
    return response

def artist_profile(request):
    response = render(request, 'artistAccount.html')
    return response

def gigs(request):
    response = render(request, 'gigs.html')
    return response

def gig(request):
    return HttpResponse("The gig page works")

def map(request):
    return HttpResponse("The map page works")

