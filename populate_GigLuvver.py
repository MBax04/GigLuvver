import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GigLuvver.settings')

import django
django.setup()
from gigluvver_app.models import Performer, Venue, Gig, Attendee
from django.contrib.auth.models import User
from django.core.files import File
from datetime import datetime, time

def populate():
    
    performer_data = [
        {'username': 'Queen', 'email': 'queen@gmail.com', 'password': 'Qu33n123',
        'stage_name': 'Queen', 'genre': 'Rock', 'profile_picture_path': './media/profile_images/queen_logo.jpg'},
        {'username': 'Muse', 'email': 'queen@gmail.com', 'password': 'Password123',
        'stage_name': 'Muse', 'genre': 'Rock', 'profile_picture_path': './media/profile_images/muse_logo.jpg'},
        {'username': 'Billie Joe Armstrong', 'email': 'day@gmail.com', 'password': '12345678',
        'stage_name': 'Green Day', 'genre': 'Pop Punk', 'profile_picture_path': './media/profile_images/green_day_logo.png'},
    ]

    for data in performer_data:
        user, created = User.objects.get_or_create(username=data['username'], email=data['email'])
        if created:
            user.set_password(data['password'])
            user.save()
        performer, created = Performer.objects.get_or_create(User=user, StageName=data['stage_name'], Genre=data['genre'])
        if created:
            profile_picture_path = data['profile_picture_path']
            with open(profile_picture_path, 'rb') as f:
                performer.ProfilePicture.save(os.path.basename(profile_picture_path), File(f))


    venue_data = [
        {'name': 'QMU', 'location': '22 University Gardens, Glasgow G12 8QN'},
        {'name': 'Barrowland Ballroom', 'location': '244 Gallowgate, Glasgow G4 0TT'},
        {'name': 'Hydro', 'location': 'Exhibition Way, Stobcross Rd, Glasgow G3 8YW'},
        {'name': 'Bellahouston Park', 'location': '16 Dumbreck Rd, Bellahouston, Glasgow G41 5BW'},
        {'name': 'King Tuts Wah Wah Hut', 'location': '272A St Vincent St, Glasgow G2 5RL'}
    ]

    for data in venue_data:
        Venue.objects.get_or_create(VenueName=data['name'], Location=data['location'])

    gig_data = [
        {'gig_id': '0001', 'name': 'Queen at the QMU', 'date': datetime(2024, 7, 17), 'time': time(hour=20, minute=0),
         'performers': [Performer.objects.get(StageName='Queen')], 
         'venue': Venue.objects.get(VenueName='QMU'), 'gig_picture_path': './media/gig_images/queen_gig.jpg'},
        {'gig_id': '0002', 'name': 'Muse and Green Day', 'date': datetime(2024, 9, 3), 'time': time(hour=19, minute=30),
         'performers': [Performer.objects.get(StageName='Muse'), Performer.objects.get(StageName='Green Day')], 
         'venue': Venue.objects.get(VenueName='Hydro'), 'gig_picture_path': './media/gig_images/hella_mega_tour.jpg'},
         {'gig_id': '0003', 'name': 'Will of the People World Tour', 'date': datetime(2024, 4, 27), 'time': time(hour=16, minute=45),
         'performers': [Performer.objects.get(StageName='Muse')], 
         'venue': Venue.objects.get(VenueName='Bellahouston Park'), 'gig_picture_path': './media/gig_images/will_of_the_people.jpg'},
    ]

    for data in gig_data:
        gig, created = Gig.objects.get_or_create(GigID=data['gig_id'], GigName=data['name'], Date=data['date'], Time=data['time'], Venue=data['venue'])
        if created:
            gig.PerformersStageNames.add(*data['performers'])
            gig_picture_path = data['gig_picture_path']
            with open(gig_picture_path, 'rb') as f:
                gig.GigPicture.save(os.path.basename(gig_picture_path), File(f))


    attendee_data = [
        {'username': 'Michael', 'email': 'michael@gmail.com', 'password': 'michael1234',
        'gigs': [Gig.objects.get(GigName='Queen at the QMU'), Gig.objects.get(GigName='Muse and Green Day'), Gig.objects.get(GigName='Will of the People World Tour')],
        'profile_picture_path': './media/profile_images/michael.png'},
        {'username': 'Paul', 'email': 'paul@gmail.com', 'password': '12paul34',
        'gigs': [Gig.objects.get(GigName='Will of the People World Tour')],
        'profile_picture_path': './media/profile_images/paul.png'},
        {'username': 'Lewis', 'email': '', 'password': 'l3w1s',
        'gigs': [Gig.objects.get(GigName='Muse and Green Day'), Gig.objects.get(GigName='Queen at the QMU')],
        'profile_picture_path': './media/profile_images/lewis.png'},
        {'username': 'Alasdair', 'email': 'Alasdair@gmail.com', 'password': 'A1asda1r',
        'gigs': [Gig.objects.get(GigName='Queen at the QMU')],
        'profile_picture_path': './media/profile_images/alasdair.png'},
    ]

    for data in attendee_data:
        user, created = User.objects.get_or_create(username=data['username'], email=data['email'])
        if created:
            user.set_password(data['password'])
            user.save()
        attendee, created = Attendee.objects.get_or_create(User=user)
        if created:
            attendee.Gigs.add(*data['gigs'])
            profile_picture_path = data['profile_picture_path']
            with open(profile_picture_path, 'rb') as f:
                attendee.ProfilePicture.save(os.path.basename(profile_picture_path), File(f))


if __name__ == '__main__':
    print('Starting GigLuvver population script...')
    populate()
    print("Finished")