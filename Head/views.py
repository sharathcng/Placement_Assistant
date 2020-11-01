from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Student.models import *
# Create your views here.


def D_Head(request):  # Drive Head Html Page.
    return render(request, "Drives/DriveHead.html")

@login_required
def Students(request):
    year = Student_Profile.objects.values('batch').distinct()
    return render(request, "Admin/dashboard.html", {'year':year})


@login_required
def Students_List(request,batch):
    students = Student_Profile.objects.filter(batch=batch)
    return render(request, "Admin/studentsList.html", {'students':students,'batch':batch})

@login_required
def Students_Details(request,id):
    students = User.objects.filter(id = id)
    profile = Student_Profile.objects.filter(username = id)
    academic = Academic_table.objects.filter(username = id)
    skill = skills.objects.filter(username = id)
    project = projects.objects.filter(username = id)
    return render(request, "Admin/studentDetails.html",{'students':students,'profile':profile,
                                                    'skill':skill,'project':project,
                                                    'academic':academic
                                                } 
                )
