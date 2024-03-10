from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Performer(models.Model):
    UserName = models.CharField(max_length=128, unique=True)
    StageName = models.CharField(max_length=128)
    Genre = models.CharField(max_length=128)
    ProfilePicture = models.ImageField(upload_to='./media/profile_images', blank=True)

    def __str__(self):
        return self.StageName


class Venue(models.Model):
    VenueName = models.CharField(max_length=128, unique=True)
    Location = models.CharField(max_length=128)

    def __str__(self):
        return self.VenueName


class Gig(models.Model):
    GigID = models.CharField(max_length=128, unique=True)
    GigName = models.CharField(max_length=128, default="Default Name")
    Date = models.DateField()
    Time = models.TimeField()
    PerformersStageNames = models.ManyToManyField(Performer)
    GigPicture = models.ImageField(upload_to='./media/gig_images', blank=True)
    Venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return self.GigName


class Attendee(models.Model):
    UserName = models.CharField(max_length=128, unique=True)
    Gigs = models.ManyToManyField(Gig)

    def __str__(self):
        return self.UserName