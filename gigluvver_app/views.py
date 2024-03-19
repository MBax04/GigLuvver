from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from gigluvver_app.forms import UserForm, ArtistProfileForm, UserProfileForm, GigForm
from django.contrib.auth.decorators import login_required
from gigluvver_app.models import Gig, Performer, Venue, UserProfile, Attendees
from django.db.models import Count


def home(request):
    context_dict = {}
    context_dict['profile'] = get_profile(request)

    upcoming_gigs_list = Gig.objects.order_by('Date')[:5]
    context_dict['upcoming_gigs'] = upcoming_gigs_list
    popular_gigs_list = Gig.objects.annotate(num_attendees=Count('attendees')).order_by('-num_attendees')[:5]
    context_dict['popular_gigs'] = popular_gigs_list

    response = render(request, 'home.html', context_dict)
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
        response = render(request, 'user_login.html', context={'profile':get_profile(request)})
        return response

@login_required
def log_out(request):
    logout(request)
    return redirect(reverse('gigluvver_app:home'))

@login_required
def my_tickets(request):
    context_dict = {}

    context_dict['profile'] = get_profile(request)
    gig_list = Gig.objects.filter(attendees__Attendee=context_dict['profile'])
    context_dict['gigs'] = gig_list

    response = render(request, 'tickets.html', context=context_dict)
    return response

@login_required
def user_profile(request):
    user_profile = get_profile(request)
    context = {'profile':get_profile(request),
               'profile_picture':user_profile.ProfilePicture}
    return render(request, 'account.html', context)

def create_account(request):
    return HttpResponse("The create_account page works")

def create_user_account(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            if profile_form.is_valid():
                user_profile = profile_form.save(commit=False)
                user_profile.UserField = user
                user_profile.save()

                registered = True
            else:
                print(profile_form.errors)
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    response = render(request, 'create_user_account.html',
                      context = {'user_form': user_form,
                                 'profile_form': profile_form,
                                 'registered': registered,
                                 'profile':get_profile(request)})
    return response

def create_artist_account(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ArtistProfileForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            if profile_form.is_valid():
                user_profile = profile_form.save(commit=False)
                user_profile.IsPerformer = True
                if 'picture' in request.FILES:
                    user_profile.picture = request.FILES['picture']
                user_profile.UserField = user

                user_profile.save()

                registered = True
            else:
                print(profile_form.errors)
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        profile_form = ArtistProfileForm()
        
    response = render(request, 'create_artist_account.html',
                      context = {'user_form': user_form,
                                 'profile_form': profile_form,
                                 'registered': registered,
                                 'profile':get_profile(request)})
    return response

def artist_log_in(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_authenticated:
                login(request, user)
                #profile = user.get_profile()
                return redirect(reverse('gigluvver_app:home'))
                #else:
                #    return HttpResponse("Your account is not an artist account. Try signing in as a user.")
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        response = render(request, 'artist_login.html', context={'profile':get_profile(request)})
        return response

@login_required
def my_gigs(request):
    context_dict = {}

    context_dict['profile'] = get_profile(request)

    gig_list = Gig.objects.filter(performer__Performers=context_dict['profile'] ).order_by('Date')
    context_dict['gigs'] = gig_list
    response = render(request, 'my_gigs.html', context=context_dict)
    return response

@login_required
def artist_profile(request):
    user_profile = get_profile(request)
    context = {'profile_picture': user_profile.ProfilePicture,
               'profile':user_profile}
    return render(request, 'artistAccount.html', context)

def gigs(request):
    context_dict = {}

    gig_list = Gig.objects.all()
    context_dict['gigs'] = gig_list
    venue_list = Venue.objects.all()
    context_dict['venues'] = venue_list
    performer_list = UserProfile.objects.filter(IsPerformer=True)
    context_dict['performers'] = performer_list
    genre_list = UserProfile.objects.values_list('Genre', flat=True).distinct()
    genre_list = list(filter(lambda x: x != '', genre_list))
    context_dict['genres'] = genre_list
    context_dict['profile'] = get_profile(request)
    gig_performers_list = Performer.objects.all()
    context_dict['gig_performers'] = gig_performers_list

    context_performers = {}
    for gig in gig_performers_list:
        performers = gig.Performers.all()
        key = 'a' + str(gig.id)
        context_performers[key] = performers
    context_dict['context_performers'] = context_performers

    response = render(request, 'gigs.html', context=context_dict)
    return response

def gig(request, gig_id):
    context_dict = {}

    gig = Gig.objects.get(id=gig_id)
    context_dict['gig'] = gig
    performer = Performer.objects.get(PerformerGig=gig)
    performer_list = performer.Performers.all()
    context_dict['performers'] = performer_list
    context_dict['profile'] = get_profile(request)
    context_dict['gig_picture'] = gig.GigPicture
    num_going = Attendees.objects.filter(Gigs=gig).count()
    context_dict['num_going'] = num_going
    
    response = render(request, 'gig.html', context=context_dict)
    return response

def map(request):
    return HttpResponse("The map page works")

def change_profile_picture(request):
    context={'profile':get_profile(request)}
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            user_profile = UserProfile.objects.get(UserField=request.user)
            user_profile.ProfilePicture = profile_picture
            user_profile.save()
            return redirect('gigluvver_app:success_page')
    return render(request, 'change_profile_picture.html',context=context)

def success_page(request):
    response = render(request, 'success_page.html')
    return response


def create_gig(request):
    form = GigForm()
    if request.method == 'POST':
        form = GigForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/gigluvver_app/')
        else:
            print(form.errors)
    return render(request, 'create_gig.html', context={'profile':get_profile(request), 'form':form})

def get_profile(request):
    try:
        if request.user.is_authenticated:
            return UserProfile.objects.get(UserField=request.user)
        else:
            return None
    except UserProfile.DoesNotExist:
        return None
