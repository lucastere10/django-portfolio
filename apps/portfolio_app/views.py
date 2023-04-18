from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'portfolio_app/home.html')

def projects(request):
    return render(request, 'portfolio_app/projects.html')

def post(request):
    return render(request, 'portfolio_app/post.html')

def profile(request):
    return render(request, 'portfolio_app/profile.html')

