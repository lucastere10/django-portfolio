from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("post/<str:pk>", views.post, name="post"),
    path("resume/", views.resume, name = 'resume'),
    path("contact/", views.contact, name = 'contact'),

    #CRUD PATHS
    path("create_post/", views.createPost, name='create_post'),
    path("update_post/<str:pk>", views.updatePost, name='update_post'),
    path("delete_post/<str:pk>", views.deletePost, name='delete_post'),

    #EMAIL
    path('send_email/', views.sendEmail, name='send_email'),
]