from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def Notification(request):
    return render(request,"Notifications/notification.html")
