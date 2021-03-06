from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login),
    path("home", views.home),
    path("logout", views.logout),
    path("newCamp", views.newCamp),
    path("newChar", views.newChar),
]
