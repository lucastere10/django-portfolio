from django.shortcuts import render, redirect
from . forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, SocialsUpdateForm, HomeUpdateForm, ResumeUpdateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . models import PageProfile
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/user/edit_profile/')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})

def profile(request):
    profile = PageProfile.objects.get(name="Lucas Caldas")

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES)
        s_form = SocialsUpdateForm(request.POST)
        h_form = HomeUpdateForm(request.POST, request.FILES)
        r_form = ResumeUpdateForm(request.POST)
        if u_form.is_valid() and p_form.is_valid() and s_form.is_valid() and h_form.is_valid() and r_form.is_valid():
            u_form.save()
            p_form.save()
            s_form.save()
            h_form.save()
            r_form.save()
            return redirect('/home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
        s_form = SocialsUpdateForm()
        h_form = HomeUpdateForm()
        r_form = ResumeUpdateForm()

    context = {
        'profile':profile,
        'u_form':u_form,
        'p_form':p_form,
        's_form':s_form,
        'h_form':h_form,
        'r_form':r_form,
    }

    return render(request, 'registration/edit_profile.html', context)