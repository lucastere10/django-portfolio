from django.shortcuts import render, redirect
from . forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

'''def login(request):
    return render(request, 'user_app/login.html')

def register(request):
    return render(request, 'user_app/register.html')'''

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})