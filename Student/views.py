from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Student.models import *

# Create your views here.


def D_Student(request):  # Drive Stundent Html Page.
    return render(request, "Drives/DriveStudent.html")


def Profile(request):  # Stundent profile Html Page.
    user = User.objects.filter(username = request.user)
    profile = Student_Profile.objects.filter(username = request.user)
    academic = Academic_table.objects.filter(username = request.user)
    skill = skills.objects.filter(username = request.user)
    project = projects.objects.filter(username = request.user)
    context = {'user': user, 'profile': profile,
               'skill': skill, 'project': project,
               'academic': academic
               }
    return render(request, "Student/profile.html",context 
                )
