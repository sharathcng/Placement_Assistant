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
def Drives(request):  # Drive Head Html Page.
    return render(request, "Drives/driveBase.html")


@login_required(login_url='login')
def Add_Drive(request): 
    context={}
    if request.method == "post":
        form = CompanyForms(request.POST)  # , request.FILES
        if form.is_valid():
            form.save()
        return redirect('CriteriaDetails')
    else: 
        form = CompanyForms()
        context['form'] = form
        return render(request, "Drives/addDrive.html", context)


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
        