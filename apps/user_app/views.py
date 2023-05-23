from django.shortcuts import render, redirect
from . forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
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

def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('/home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request, 'registration/edit_profile.html', context)