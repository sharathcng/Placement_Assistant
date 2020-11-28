from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from Notifications.models import *
from Drives.models import *
from django.http import HttpResponse

from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Notification(request):
    notificate = Notifications.objects.all()
    offer = drive.objects.filter(username=request.user)
    return render(request,"Notifications/notification.html",{"notificate":notificate,"offer":offer})

def notificationForm(request):
    return render(request,"Notifications/notificationForm.html")

@login_required(login_url='login')
def postNotification(request):
    if request.method == "POST":
        Notifications.objects.create(username=request.user,subject=request.POST['subject'],body=request.POST['body'])
        print('saved')
        return redirect(Notification)
    else:   
        return render(request,"Notifications/notificationForm.html")
    
@login_required(login_url='login')
def notificationDetails(request,id):
    notifyDetails = Notifications.objects.filter(id=id)
    return render(request,"Notifications/notificationDetails.html",{"notifyDetails":notifyDetails})

@login_required(login_url='login')
def applyJob(request,id,x):
    drive.objects.filter(username=request.user,Company_Name=id).update(Selected_status=x)
    return redirect(Notification)

