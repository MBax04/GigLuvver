from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

class ArtistProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	stageName = models.CharField(max_length=30)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __str__(self):
		return self.user.username
