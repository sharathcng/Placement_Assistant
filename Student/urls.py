from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('D_Student', views.D_Student, name="D_Student"),
    path('Profile', views.Profile, name="Profile"),
]
