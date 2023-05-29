from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#LOGIN URL ARE MADE BY DJANGO AUTH IN SETTINGS.URL FILE
'''urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
]'''

urlpatterns = [
    path("register/", views.registration, name = 'register'),
    path("edit_profile/", views.profile, name = 'edit_profile')
]