from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    UserField = models.OneToOneField(User, on_delete=models.CASCADE)
    IsPerformer = models.BooleanField(default=False)
    StageName = models.CharField(max_length=128, unique=True, blank=True, null=True)
    Genre = models.CharField(max_length=128, blank=True)
    ProfilePicture = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        if self.IsPerformer:
            return self.StageName
        else:
            return self.UserField.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not hasattr(self, 'Attendees'):
            Attendees.objects.get_or_create(Attendee=self)

    def delete(self, *args, **kwargs):
        if self.ProfilePicture:
            self.ProfilePicture.delete()
        super().delete(*args, **kwargs)

class Venue(models.Model):
    VenueName = models.CharField(max_length=128, unique=True)
    Location = models.CharField(max_length=128)

    def __str__(self):
        return self.VenueName

class Gig(models.Model):
    GigName = models.CharField(max_length=128, default="Default Name", unique=True)
    Date = models.DateField()
    Time = models.TimeField()
    GigPicture = models.ImageField(upload_to='gig_images/', blank=True)
    Venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return self.GigName

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not hasattr(self, 'Performer'):
            Performer.objects.get_or_create(PerformerGig=self)

class Attendees(models.Model):
    Attendee = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    Gigs = models.ManyToManyField(Gig, blank=True)

    def __str__(self):
        return str(self.Attendee)

class Performer(models.Model):
    PerformerGig = models.OneToOneField(Gig, on_delete=models.CASCADE)
    Performers = models.ManyToManyField(UserProfile, blank=True, limit_choices_to={'IsPerformer': True})

    def __str__(self):
        return str(self.PerformerGig)

    