from django.contrib import admin
from gigluvver_app.models import UserProfile, Gig, Attendees, Performer, Venue

admin.site.register(UserProfile)
admin.site.register(Gig)
admin.site.register(Venue)
admin.site.register(Attendees)
admin.site.register(Performer)
