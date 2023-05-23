from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    #fk reletionship
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    birthdate = models.DateTimeField(help_text = 'your birthday :)', null = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    name = models.CharField(max_length = 200, null = True)
    #contact info
    adress =  models.CharField(max_length = 200, null = True)
    phone =  models.CharField(max_length = 200, null = True)
    #email = models.EmailField(User.email, null = True)
    #personal info
    thumbnail = models.ImageField(default = 'UserProfile.png', upload_to ='users/thumb', null=True, blank=True,)
    #first_name = models.CharField(User.first_name, max_length = 200, null = True)
    #last_name = models.CharField(User.last_name, max_length = 200, null = True)
    #socials
    insta = models.URLField(max_length = 200, null = True)
    git = models.URLField(max_length = 200, null = True)
    linkedin = models.URLField(max_length = 200, null = True)
	#resume
    subtitle =  models.CharField(max_length = 200, null = True)
    skills =  models.TextField(null = True)
    education =  models.TextField(null = True)
    languages =  models.TextField(null = True)

    def __str__(self):
        return self.user.username
 



