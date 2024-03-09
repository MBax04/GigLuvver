from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    response = render(request, 'home.html')
    return response

def log_in(request):
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
    response = render(request, 'create_user_account.html')
    return response

def create_artist_account(request):
    response = render(request, 'create_artist_account.html')
    return response

def artist_log_in(request):
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
    response = render(request, 'gig.html')
    return response

def map(request):
    return HttpResponse("The map page works")