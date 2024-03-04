from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("The Home page works <a href='/gigluvver_app/log_in/'>About</a>")


def log_in(request):
    return HttpResponse("The log_in page works")

def my_tickets(request):
    return HttpResponse("The my_tickets page works")

def user_profile(request):
    return HttpResponse("The user_profile page works")

def create_account(request):
    return HttpResponse("The create_account page works")

def create_user_account(request):
    return HttpResponse("The create_user_account page works")

def create_artist_account(request):
    return HttpResponse("The create_artist_account page works")

def artist_log_in(request):
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