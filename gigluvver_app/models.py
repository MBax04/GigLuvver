from django.db import models

# Create your models here.
class Gig(models.Model):
    GigID = models.CharField(max_length=128, unique=True)
    Date = models.Date()
    Time = models.Time()
    PerformerStageNames = models.CharField(max_length=128)
    ProfilePicture = models.ImageField(upload_to='gig_images', blank=True)

    def __str__(self):
        return self.name


class Attendee(models.Model):
    UserName = models.CharField(max_length=128, unique=True)
    GigID = models.ForeignKey(Gig, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Performer(models.Model):
    UserName = models.CharField(max_length=128, unique=True)
    StageName = models.CharField(max_length=128)
    Genre = models.CharField(max_length=128)
    ProfilePicture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.name


class Venue(models.Model):
    VenueName = models.CharField(max_length=128, unique=True)
    Location = modles.CharField(max_length=128)

    def __str__(self):
        return self.name