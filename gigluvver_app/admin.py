from django.contrib import admin
from gigluvver_app.models import Gig, Attendee, Performer, Venue

admin.site.register(Gig)
admin.site.register(Attendee)
admin.site.register(Performer)
admin.site.register(Venue)
