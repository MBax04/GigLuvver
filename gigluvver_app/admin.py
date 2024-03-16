from django.contrib import admin
from gigluvver_app.models import UserProfile, Gig, Attendees, Performer, Venue

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('UserField', 'id')
    readonly_fields = ('id',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Gig)
admin.site.register(Venue)
admin.site.register(Attendees)
admin.site.register(Performer)
