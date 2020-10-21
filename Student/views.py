from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Student.models import Student_Profile
# Create your views here.


def D_Student(request):  # Drive Stundent Html Page.
    return render(request, "Drives/DriveStudent.html")


def Profile(request):  # Stundent profile Html Page.
    user = User.objects.filter(username = request.user)
    profile = Student_Profile.objects.filter(username = request.user)
    return render(request, "Student/profile.html",{'user':user,'profile':profile})
