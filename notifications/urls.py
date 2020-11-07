from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("notification", views.Notification, name="notification")
]
