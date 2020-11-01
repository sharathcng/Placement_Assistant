from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Student.models import *
from django.http import HttpResponse
from .forms import CompanyForms, TestForms, CriteriaForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
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

@login_required(login_url='login')
def Companydetails(request): 
    context={}
    if request.method == "post":
        form = CompanyForms(request.POST)  # , request.FILES
        if form.is_valid():
            form.save()
        return redirect('CriteriaDetails')
    else: 
        form = CompanyForms()
        context['form'] = form
        return render(request, "Drives/CompanyDetails.html", context)


@login_required(login_url='login')
def Testdetails(request):
    context = {}
    if request.method == "post":
        form = TestForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('D_Head')
    else:
        form = TestForms()
        context['form'] = form
        return render(request, "Drives/TestDetails.html", context)
        


@login_required(login_url='login')
def Criteriadetails(request):
    context = {}
    if request.method == "post":
        form = CriteriaForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Testdetails')
    else:
        form = CriteriaForms()
        context['form']=form
        return render(request, "Drives/CriteriaDetails.html", context)
        
