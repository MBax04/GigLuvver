import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GigLuvver.settings')

import django
django.setup()
from gigluvver_app.models import UserProfile, Venue, Gig, Attendees, Performer
from django.contrib.auth.models import User
from django.core.files import File
from datetime import datetime, time

def populate():
    
    user_profile_data = [
        {'username': 'Queen', 'email': 'queen@gmail.com', 'password': 'Qu33n123', 'is_performer': True,
            'stage_name': 'Queen', 'genre': 'Rock', 'profile_picture_path': './media/profile_images/queen_logo.jpg'},
        {'username': 'Muse', 'email': 'muse@gmail.com', 'password': 'Password123', 'is_performer': True,
            'stage_name': 'Muse', 'genre': 'Rock', 'profile_picture_path': './media/profile_images/muse_logo.jpg'},
        {'username': 'Billie Joe Armstrong', 'email': 'day@gmail.com', 'password': '12345678', 'is_performer': True,
            'stage_name': 'Green Day', 'genre': 'Punk', 'profile_picture_path': './media/profile_images/green_day_logo.png'},
        {'username': 'Taylor Swift', 'email': 'swift@gmail.com', 'password': '12345678', 'is_performer': True,
            'stage_name': 'Taylor Swift', 'genre': 'Pop', 'profile_picture_path': './media/profile_images/taylor_swift_logo.png'},
        {'username': 'Justin Bieber', 'email': 'bieber@gmail.com', 'password': '12345678', 'is_performer': True,
            'stage_name': 'Justin Bieber', 'genre': 'Pop', 'profile_picture_path': './media/profile_images/justin_bieber_logo.png'},
        {'username': 'AC/DC', 'email': 'DC@gmail.com', 'password': '12345', 'is_performer': True,
            'stage_name': 'AC/DC', 'genre': 'Rock', 'profile_picture_path': './media/profile_images/ac_dc_logo.png'},
        {'username': 'Metallica', 'email': 'metallica@gmail.com', 'password': '12345', 'is_performer': True,
            'stage_name': 'Metallica', 'genre': 'Metal', 'profile_picture_path': './media/profile_images/metallica_logo.png'},
        {'username': 'Iron Maiden', 'email': 'iron@gmail.com', 'password': '12345', 'is_performer': True,
            'stage_name': 'Iron Maiden', 'genre': 'Metal', 'profile_picture_path': './media/profile_images/iron_maiden_logo.png'},
        {'username': 'The Killers', 'email': 'killers@gmail.com', 'password': '12345', 'is_performer': True,
            'stage_name': 'The Killers', 'genre': 'Indie', 'profile_picture_path': './media/profile_images/the_killers_logo.png'},
        {'username': 'The Strokes', 'email': 'strokes@gmail.com', 'password': '12345', 'is_performer': True,
            'stage_name': 'The Strokes', 'genre': 'Indie', 'profile_picture_path': './media/profile_images/the_strokes_logo.png'},

        {'username': 'Michael', 'email': 'michael@gmail.com', 'password': 'michael1234', 'is_performer': False,
            'profile_picture_path': './media/profile_images/michael.png'},
        {'username': 'Paul', 'email': 'paul@gmail.com', 'password': '12paul34', 'is_performer': False,
            'profile_picture_path': './media/profile_images/paul.png'},
        {'username': 'Lewis', 'email': 'lewis@gmail.com', 'password': 'l3w1s', 'is_performer': False,
            'profile_picture_path': './media/profile_images/lewis.png'},
        {'username': 'Alasdair', 'email': 'Alasdair@gmail.com', 'password': 'A1asda1r', 'is_performer': False,
            'profile_picture_path': './media/profile_images/alasdair.png'},
    ]

    for data in user_profile_data:
        user, created = User.objects.get_or_create(username=data['username'], email=data['email'])
        if created:
            user.set_password(data['password'])
            user.save()
        user_profile, created = UserProfile.objects.get_or_create(UserField=user, IsPerformer=data['is_performer'])
        if created:
            if data['is_performer']:
                user_profile.StageName = data['stage_name']
                user_profile.Genre = data['genre']
                user_profile.save()

            profile_picture_path = data['profile_picture_path']
            with open(profile_picture_path, 'rb') as f:
                user_profile.ProfilePicture.save(os.path.basename(profile_picture_path), File(f))


    venue_data = [
        {'name': 'QMU', 'location': '22 University Gardens, Glasgow G12 8QN', 'position':'55.8736686706543,-4.291417121887207'},
        {'name': 'Barrowland Ballroom', 'location': '244 Gallowgate, Glasgow G4 0TT', 'position':'55.8553466796875,-4.23670768737793'},
        {'name': 'Hydro', 'location': 'Exhibition Way, Stobcross Rd, Glasgow G3 8YW', 'position':'55.8597412109375,-4.285629749298096'},
        {'name': 'Bellahouston Park', 'location': '16 Dumbreck Rd, Bellahouston, Glasgow G41 5BW', 'position':'55.84640884399414,-4.314202785491943'},
        {'name': 'King Tuts Wah Wah Hut', 'location': '272A St Vincent St, Glasgow G2 5RL', 'position':'55.86256408691406,-4.265017509460449'}
    ]

    for data in venue_data:
        Venue.objects.get_or_create(VenueName=data['name'], Location=data['location'], Position=data['position'])

    gig_data = [
        {'name': 'Queen at the QMU', 'date': datetime(2024, 7, 17), 'time': time(hour=20, minute=0),
            'venue': Venue.objects.get(VenueName='QMU'), 'gig_picture_path': './media/gig_images/queen_gig.jpg'},
        {'name': 'Muse and Green Day', 'date': datetime(2024, 9, 3), 'time': time(hour=19, minute=30),
            'venue': Venue.objects.get(VenueName='Hydro'), 'gig_picture_path': './media/gig_images/green_day_gig.png'},
        {'name': 'Will of the People World Tour', 'date': datetime(2024, 4, 27), 'time': time(hour=16, minute=45),
            'venue': Venue.objects.get(VenueName='Bellahouston Park'), 'gig_picture_path': './media/gig_images/will_of_the_people.jpg'},
        {'name': 'Rock Show', 'date': datetime(2024, 2, 12), 'time': time(hour=21, minute=0),
            'venue': Venue.objects.get(VenueName='Barrowland Ballroom'), 'gig_picture_path': './media/gig_images/rock_show.jfif'},
        {'name': 'Eras Tour', 'date': datetime(2024, 8, 28), 'time': time(hour=22, minute=0),
            'venue': Venue.objects.get(VenueName='Hydro'), 'gig_picture_path': './media/gig_images/eras_tour.jfif'},
        {'name': 'Metallica', 'date': datetime(2024, 4, 11), 'time': time(hour=20, minute=0),
            'venue': Venue.objects.get(VenueName='King Tuts Wah Wah Hut'), 'gig_picture_path': './media/gig_images/metallica_show.jfif'},
        {'name': 'Iron Maiden', 'date': datetime(2024, 11, 22), 'time': time(hour=19, minute=0),
            'venue': Venue.objects.get(VenueName='QMU'), 'gig_picture_path': './media/gig_images/iron_maiden_show.jfif'},
        {'name': 'Metal Show', 'date': datetime(2024, 10, 9), 'time': time(hour=23, minute=0),
            'venue': Venue.objects.get(VenueName='Bellahouston Park'), 'gig_picture_path': './media/gig_images/metal_show.jfif'},
        {'name': 'The Killers', 'date': datetime(2024, 4, 12), 'time': time(hour=20, minute=0),
            'venue': Venue.objects.get(VenueName='King Tuts Wah Wah Hut'), 'gig_picture_path': './media/gig_images/the_killers_show.jfif'},
        {'name': 'The Strokes', 'date': datetime(2024, 12, 22), 'time': time(hour=19, minute=0),
            'venue': Venue.objects.get(VenueName='QMU'), 'gig_picture_path': './media/gig_images/the_strokes_show.jfif'},
        {'name': 'Indie Show', 'date': datetime(2024, 1, 9), 'time': time(hour=23, minute=0),
            'venue': Venue.objects.get(VenueName='Barrowland Ballroom'), 'gig_picture_path': './media/gig_images/indie_show.jfif'},
        {'name': 'Justin Bieber', 'date': datetime(2025, 2, 14), 'time': time(hour=22, minute=30),
            'venue': Venue.objects.get(VenueName='Bellahouston Park'), 'gig_picture_path': './media/gig_images/justin_bieber_show.jfif'},
    ]

    for data in gig_data:
        gig, created = Gig.objects.get_or_create(GigName=data['name'], Date=data['date'], Time=data['time'], Venue=data['venue'])
        if created:
            gig_picture_path = data['gig_picture_path']
            with open(gig_picture_path, 'rb') as f:
                gig.GigPicture.save(os.path.basename(gig_picture_path), File(f))


    attendees_data = [
        {'attendee': 'Michael',
            'gigs': [Gig.objects.get(GigName='Queen at the QMU'), Gig.objects.get(GigName='Muse and Green Day'),
                    Gig.objects.get(GigName='Will of the People World Tour'), Gig.objects.get(GigName='Rock Show'),
                    Gig.objects.get(GigName='Metallica'), Gig.objects.get(GigName='Iron Maiden'),
                    Gig.objects.get(GigName='Metal Show'), Gig.objects.get(GigName='The Killers'),
                    Gig.objects.get(GigName='The Strokes'), Gig.objects.get(GigName='Indie Show')]},
        {'attendee': 'Paul',
            'gigs': [Gig.objects.get(GigName='Will of the People World Tour'), Gig.objects.get(GigName='Eras Tour'),
                    Gig.objects.get(GigName='Justin Bieber'), Gig.objects.get(GigName='The Killers')]},
        {'attendee': 'Lewis',
            'gigs': [Gig.objects.get(GigName='Muse and Green Day'), Gig.objects.get(GigName='Queen at the QMU'),
                    Gig.objects.get(GigName='Eras Tour'), Gig.objects.get(GigName='Rock Show'),
                    Gig.objects.get(GigName='Metal Show'), Gig.objects.get(GigName='Indie Show')]},
        {'attendee': 'Alasdair',
            'gigs': [Gig.objects.get(GigName='Queen at the QMU')]},
        {'attendee': 'Queen',
            'gigs': [Gig.objects.get(GigName='Eras Tour'), Gig.objects.get(GigName='Rock Show')]},
        {'attendee': 'Muse',
            'gigs': [Gig.objects.get(GigName='Metal Show'), Gig.objects.get(GigName='Rock Show')]},
        {'attendee': 'Billie Joe Armstrong',
            'gigs': [Gig.objects.get(GigName='Muse and Green Day'), Gig.objects.get(GigName='Eras Tour')]},
    ]

    for data in attendees_data:
        attendee = Attendees.objects.get(Attendee=UserProfile.objects.get(UserField=User.objects.get(username=data['attendee'])))
        attendee.Gigs.add(*data['gigs'])

    
    performer_data = [
        {'gig': 'Queen at the QMU',
            'performers': [UserProfile.objects.get(StageName='Queen')]},
        {'gig': 'Muse and Green Day',
            'performers': [UserProfile.objects.get(StageName='Muse'), UserProfile.objects.get(StageName='Green Day')]},
        {'gig': 'Will of the People World Tour',
            'performers': [UserProfile.objects.get(StageName='Muse')]},
        {'gig': 'Rock Show',
            'performers': [UserProfile.objects.get(StageName='Muse'), UserProfile.objects.get(StageName='Queen'), UserProfile.objects.get(StageName='AC/DC')]},
        {'gig': 'Eras Tour',
            'performers': [UserProfile.objects.get(StageName='Taylor Swift')]},
        {'gig': 'Metallica',
            'performers': [UserProfile.objects.get(StageName='Metallica')]},
        {'gig': 'Iron Maiden',
            'performers': [UserProfile.objects.get(StageName='Iron Maiden')]},
        {'gig': 'Metal Show',
            'performers': [UserProfile.objects.get(StageName='Metallica'), UserProfile.objects.get(StageName='Iron Maiden')]},
        {'gig': 'The Killers',
            'performers': [UserProfile.objects.get(StageName='The Killers')]},
        {'gig': 'The Strokes',
            'performers': [UserProfile.objects.get(StageName='The Strokes')]},
        {'gig': 'Indie Show',
            'performers': [UserProfile.objects.get(StageName='The Killers'), UserProfile.objects.get(StageName='The Strokes')]},
        {'gig': 'Justin Bieber',
            'performers': [UserProfile.objects.get(StageName='Justin Bieber')]},
    ]

    for data in performer_data:
        performer = Performer.objects.get(PerformerGig=Gig.objects.get(GigName=data['gig']))
        performer.Performers.add(*data['performers'])


    


if __name__ == '__main__':
    print('Starting GigLuvver population script...')
    populate()
    print("Finished")