from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("post/", views.post, name="post"),
    path("profile/", views.profile, name="profile"),
]