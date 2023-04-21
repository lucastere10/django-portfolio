from django.shortcuts import render
from django.http import HttpResponse
from .models import Tag,Post
# Create your views here.

def home(request):

    return render(request, 'portfolio_app/home.html')

def projects(request):
    posts = Post.objects.filter(active = True)
    context = {'posts':posts}
    return render(request, 'portfolio_app/projects.html',context)

def post(request, pk):
    post = Post.objects.get(id = pk)
    context= {'post':post}
    return render(request, 'portfolio_app/post.html', context)

def profile(request):
    return render(request, 'portfolio_app/profile.html')

