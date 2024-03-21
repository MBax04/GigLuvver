from django import forms
from gigluvver_app.models import UserProfile,Gig, Performer, Attendees
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class ArtistProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('StageName', 'Genre', 'ProfilePicture')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ()


class GigForm(forms.ModelForm):
	GigName = forms.CharField(max_length=200, help_text="Please enter the gig name: ")
	Date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
	Time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))


	class Meta:
		model = Gig
		fields = ('GigName', 'Date', 'Time', 'Venue', 'GigPicture')

class DeleteForm(forms.ModelForm):
	class Meta:
		model = Performer
		fields = ('PerformerGig',)

		