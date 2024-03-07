import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GigLuvver.settings')

import django
django.setup()
from gigluvver_app.models import Gig, Attendee, Venue, Performer

def populate():
    return



if __name__ == '__main__':
    print('Starting GigLuvver population script...')
    populate()