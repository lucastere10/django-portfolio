from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
# Create your views here.
from .forms import postForm
from .filters import PostFilter
from .models import Tag,Post

@login_required(login_url="../user/login")
def home(request):
    featured = Post.objects.order_by("-date")[:5]
    print(featured)
    context = {'featured':featured}
    return render(request, 'portfolio_app/home.html', context)

@login_required(login_url="../user/login")
def projects(request):
    projects = Post.objects.filter(active = True)
    myFilter = PostFilter(request.GET, queryset=projects)
    projects = myFilter.qs

    page = request.GET.get('page')
    paginator = Paginator(projects, 6)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)


    context = {'projects':projects, 'myFilter': myFilter}
    return render(request, 'portfolio_app/projects.html',context)

@login_required(login_url="../user/login")
def post(request, pk):
    post = Post.objects.get(id = pk)
    context= {'post':post}
    return render(request, 'portfolio_app/post.html', context)

@login_required(login_url="../user/login")
def resume(request):
    return render(request, 'portfolio_app/resume.html')

@login_required(login_url="../user/login")
def contact(request):
    return render(request, 'portfolio_app/contact.html')

#CRUD VIEWS
### POST
login_required(login_url="../user/login")
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
login_required(login_url="../user/login")
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = postForm(instance=post)

    if request.method == 'POST':
        form = postForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
        return redirect('projects')

    context = {'form':form}
    return render(request, 'portfolio_app/post_form.html', context)

### DELETE
login_required(login_url="../user/login")
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('projects')
    context = {'item':post}
    return render(request, 'portfolio_app/post_delete.html', context)

#send Emails
def sendEmail(request):
    
    if request.method == 'post':
        
        template = render_to_string('portfolio_app/email_template.html' ,{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            subject= request.POST['subject'],
            body = template,
            from_email = settings.EMAIL_HOST_USER,
            to = ['lucasmedeiroscaldas@yahoo.com.br'],
            fail_silently = False
            )
       
        email.send()

    return render(request, 'portfolio_app/email_sent.html')