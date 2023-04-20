from django.shortcuts import render
from django.http import HttpResponse
from .models import Tag,Post
# Create your views here.

def home(request):
    return render(request, 'portfolio_app/home.html')

def projects(request):
    post = Post.objects.all()
    return render(request, 'portfolio_app/projects.html')

def post(request):
    return render(request, 'portfolio_app/post.html')

def profile(request):
    return render(request, 'portfolio_app/profile.html')

