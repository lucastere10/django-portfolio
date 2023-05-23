from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = 0)
    headline = models.CharField(max_length=100,null=False,blank=False)
    sub_headline = models.CharField(max_length=200,null=False,blank=False)
    thumbnail = models.ImageField(null=True,blank=True,upload_to='media/post_thumbs',default='default/placeholder.png')
    body = RichTextUploadingField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    active  = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    #slug =

    def __str__(self):
        return self.headline
    
    def save(self):
        super().save()

        img = Image.open(self.thumbnail.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)