from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("notification", views.Notification, name="notification"),
    path("notificationForm", views.notificationForm, name="notificationForm"),
    path("postNotification", views.postNotification, name="postNotification"),
    path("notificationDetails/<int:id>", views.notificationDetails, name="notificationDetails"),
    path("applyJob/<int:id><int:x>", views.applyJob, name="applyJob"),
    

]
