from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class PageProfile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    #personal info
    name = models.CharField(max_length = 200, null = True)
    birthdate = models.DateField(null = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    profile_img = models.ImageField(default = 'default/UserProfile.png', upload_to ='users/thumb', null=True, blank=True,)
    #contact info
    adress =  models.CharField(max_length = 200, null = True)
    phone =  PhoneNumberField(blank = True, null = True)
    #socials
    insta = models.URLField(max_length = 200, null = True)
    git = models.URLField(max_length = 200, null = True)
    linkedin = models.URLField(max_length = 200, null = True)
    #homepage
    home_img = models.ImageField(default = 'default/placeholder.png', upload_to ='users/thumb', null=True, blank=True,)
    home_skills = models.TextField(null = True)
    subtitle =  models.CharField(max_length = 200, null = True)
	#resume
    summary = models.TextField(null = True)
    skills =  models.TextField(null = True)
    experiences = models.TextField(null = True)
    education =  models.TextField(null = True)
    languages =  models.TextField(null = True)

    def __str__(self):
        return self.name



