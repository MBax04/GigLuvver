from django import forms
from gigluvver_app.models import UserProfile, ArtistProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class ArtistProfileForm(forms.ModelForm):
	class Meta:
		model = ArtistProfile
		fields = ('stageName', 'picture')