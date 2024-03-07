from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	isArtist = models.BooleanField(default=False)
	stageName = models.CharField(default='Nameless Artist', max_length=30)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __str__(self):
		return self.user.username
