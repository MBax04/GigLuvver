from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from gigluvver_app.forms import UserForm, ArtistProfileForm, UserProfileForm, GigForm, DeleteForm
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
                error_message = "Your account is disabled."
        else:
            print(f"Invalid login details: {username}, {password}")
            error_message = "Invalid login details supplied."
        profile = None
    else:
        profile = get_profile(request)
        error_message=""
    response = render(request, 'user_login.html', context={'profile':profile,'error_message':error_message})
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
                
                if 'ProfilePicture' in request.FILES:
                    profile_picture = request.FILES['ProfilePicture']
                    user_profile.ProfilePicture = profile_picture

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
        user_form = UserForm(request.POST, request.FILES)
        profile_form = ArtistProfileForm(request.POST, request.FILES)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()
            if profile_form.is_valid():
                user_profile = profile_form.save(commit=False)
                user_profile.IsPerformer = True

                if 'ProfilePicture' in request.FILES:
                    profile_picture = request.FILES['ProfilePicture']
                    user_profile.ProfilePicture = profile_picture

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
                return redirect(reverse('gigluvver_app:home'))
            else:
                error_message = "Your account is disabled."
        else:
            print(f"Invalid login details: {username}, {password}")
            error_message = "Invalid login details supplied."
        profile = None
    else:
        profile = get_profile(request)
        error_message = ""
    response = render(request, 'artist_login.html', context={'profile':profile, 'error_message':error_message})
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
    gig = Gig.objects.get(id=gig_id)
    profile = get_profile(request)
    attendee = Attendees.objects.get(Attendee=profile)

    if request.method == "POST":
        going = request.POST.getlist('goingGig')
        if len(going)==1:
            attendee.Gigs.add(gig)
        else:
            attendee.Gigs.remove(gig)

    context_dict = {}
    context_dict['gig'] = gig
    performer = Performer.objects.get(PerformerGig=gig)
    performer_list = performer.Performers.all()
    context_dict['performers'] = performer_list
    context_dict['profile'] = get_profile(request)
    context_dict['gig_picture'] = gig.GigPicture
    num_going = Attendees.objects.filter(Gigs=gig).count()
    context_dict['going'] = Attendees.objects.filter(Gigs=gig)
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
            return redirect('gigluvver_app:success_page', user_profile_id=user_profile.id)
    return render(request, 'change_profile_picture.html',context=context)

def success_page(request, user_profile_id):
    user_profile = UserProfile.objects.get(id=user_profile_id)
    context_dict = {'profile': user_profile}
    response = render(request, 'success_page.html', context=context_dict)
    return response


def create_gig(request):
    form = GigForm()
    success = True
    success_photo = True
    if request.method == 'POST':
        form = GigForm(request.POST, request.FILES)

        if form.is_valid():
            if 'GigPicture' in request.FILES:
                form.GigPicture = request.FILES['GigPicture']

                gig = form.save(commit=True)

                user = get_profile(request)

                q = UserProfile.objects.filter(id=user.id)
                
                gig.save()

                x = Performer.objects.get_or_create(PerformerGig=gig)
                x[0].Performers.set(q)

                performer = Performer.objects.get(PerformerGig=gig)
                performer.Performers.add(UserProfile.objects.get(UserField=request.user))

                return redirect('/gigluvver_app/')
            else:
                success_photo = False
        else:
            print(form.errors)
            success = False
    return render(request, 'create_gig.html', context={'profile':get_profile(request), 'form':form, 'success':success, 'success_photo':success_photo})

def delete_gig(request):
    form  = DeleteForm()

    if request.method == 'POST':
        form = DeleteForm(request.POST)

    

        user = get_profile(request)

        gig_id = form['PerformerGig'].value()
        
        print("Bleh")
        print(user.id)
        print(form["Performers"].value()[0])
        if int(form["Performers"].value()[0]) == user.id:
            Gig.objects.filter(id=gig_id).delete()
          
        

        return redirect('/gigluvver_app/')

    return render(request, 'delete_gig.html', context={'profile':get_profile(request), 'form':form})

def get_profile(request):
    try:
        if request.user.is_authenticated:
            return UserProfile.objects.get(UserField=request.user)
        else:
            return None
    except UserProfile.DoesNotExist:
        return None
    