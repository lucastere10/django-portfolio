from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import postForm
from .models import Tag,Post

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


#CRUD VIEWS
### POST
login_required(login_url='home')
def createPost(request):
    form = postForm()

    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('projects')

    context = {'form':form}
    return render(request, 'portfolio_app/post_form.html', context)

### UPDATE
login_required(login_url='home')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = postForm()

    if request.method == 'POST':
        form = postForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
        return redirect('projects')

    context = {'form':form}
    return render(request, 'portfolio_app/post_form.html', context)

### DELETE
login_required(login_url='home')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('projects')
    context = {'item':post}
    return render(request, 'portfolio_app/post_delete.html', context)