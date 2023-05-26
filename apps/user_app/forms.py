from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.contrib.auth.models import User
from .models import PageProfile


# Create your forms here.

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ["username", "email"]	
	
class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = PageProfile
		fields = ["name", "birthdate", "gender", 'profile_img']
		
class SocialsUpdateForm(forms.ModelForm):

	class Meta:
		model = PageProfile
		fields = ["adress", "phone", "insta", 'git', 'linkedin']
	
class HomeUpdateForm(forms.ModelForm):

	class Meta:
		model = PageProfile
		widgets = {
            'home_skills': SummernoteWidget(),
		}
		fields = ["home_img", "subtitle", "home_skills" ]
	
class ResumeUpdateForm(forms.ModelForm):

	class Meta:
		model = PageProfile
		widgets = {
            'summary': SummernoteWidget(),
            'skills': SummernoteWidget(),
            'experiences': SummernoteWidget(),
            'education': SummernoteWidget(),
	        'languages': SummernoteWidget(),
        }
		fields = ["summary", "skills", "experiences", 'education', 'languages']
