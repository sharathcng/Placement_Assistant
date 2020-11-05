from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Student.models import *
from django.http import HttpResponse
from .forms import PostDrive,PostTest,PostCriteria
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def Drives(request):  # Drive Head Html Page.
    return render(request, "Drives/driveBase.html")


# @login_required(login_url='login')
# def Add_Drive(request): 
#     context={}
#     if request.method == "post":
#         form = CompanyForms(request.POST)  # , request.FILES
#         if form.is_valid():
#             form.save()
#         return redirect('CriteriaDetails')
#     else: 
#         form = CompanyForms()
#         context['form'] = form
#         return render(request, "Drives/driveAdd.html", context)


# @login_required(login_url='login')
# def Testdetails(request):
#     context = {}
#     if request.method == "post":
#         form = TestForms(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('D_Head')
#     else:
#         form = TestForms()
#         context['form'] = form
#         return render(request, "Drives/TestDetails.html", context)
        


# @login_required(login_url='login')
# def Criteriadetails(request):
#     context = {}
#     if request.method == "post":
#         form = CriteriaForms(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('Testdetails')
#     else:
#         form = CriteriaForms()
#         context['form']=form
#         return render(request, "Drives/CriteriaDetails.html", context)

@login_required(login_url='login')
def Post_Drive(request):
    if request.method == "POST":
        form1 = PostDrive(request.POST)
        form2 = PostTest(request.POST)
        form3 = PostCriteria(request.POST)
        if  form1.is_valid() and form2.is_valid() and form3.is_valid() :
            a = form1.save()
            b = form2.save(commit=False)
            c = form3.save(commit=False)
            b.Company_Name = a
            b.save()
            c.Company_Name = a
            c.save()
            return redirect(Drives)
        else:
            return render(request, "Drives/driveAdd.html")
    else :
        return render(request, "Drives/driveAdd.html")





