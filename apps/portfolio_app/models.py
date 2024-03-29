from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    headline = models.CharField(max_length=100,null=False,blank=False)
    sub_headline = models.CharField(max_length=200,null=False,blank=False)
    thumbnail = models.ImageField(null=True,blank=True,upload_to='media',default='placeholder.png')
    body = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    active  = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    #slug =

    def __str__(self):
        return self.headline