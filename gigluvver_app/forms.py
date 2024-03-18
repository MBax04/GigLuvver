from django import forms
from gigluvver_app.models import UserProfile,Gig
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

class GigForm(forms.ModelForm):
	gigname = forms.CharField(max_length=200, help_text="Please enter the gig name: ")
	date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
	time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}))

	class Meta:
		model = Gig
		fields = ('gigname', 'date', 'time')