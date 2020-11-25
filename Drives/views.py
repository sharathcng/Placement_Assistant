from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Student.models import *
from Drives.models import *
from django.http import HttpResponse
from .forms import PostCompany,PostTest,PostCriteria
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def Drives(request):  # Drive Head Html Page.
    return render(request, "Drives/driveBase.html")


# new drive
@login_required(login_url='login')
def Post_Drive(request):  # posting new Drive
    if request.method == "POST":
        form1 = PostCompany(request.POST)
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

            # companyCritera = Criteria.objects.filter(id=a)
            # studentmarks = Academic_table.objects.all()
            # for course in studentmarks:
            #     if course.SSLC <= companyCritera.SSLC:
            #         if course.PUC <= companyCritera.PUC:
            #             if course.DEGREE <= companyCritera.UG:
            #                 if course.MCA <= companyCritera.PG:
            #                     form1 = drive.objects.all()
            #                     form1.Company_Name=a
            #                     form1.username = course.username
                            
        else:
            return render(request, "Drives/driveAdd.html")
    else :
        return render(request, "Drives/driveAdd.html")



@login_required(login_url='login')
def Drive_Year(request):  # company batch Html Page.
    driveYears = Company.objects.values('Year').distinct()
    return render(request, "Drives/companyBatch.html",{'driveYears':driveYears})

@login_required(login_url='login')
def Company_List(request,year):  # company list Html Page.
    companyList = Company.objects.filter(Year = year)
    testMode = Test.objects.all()
    return render(request, "Drives/companyList.html", {'companyList':companyList,
                        'year':year,'testMode':testMode})

def Drive_Details(request, id):
    companyDetails = Company.objects.filter(id=id)
    testDetails=Test.objects.filter(id=id)
    criteriaDetails=Criteria.objects.filter(id=id)
    return render(request, "Drives/ViewDrive.html", {'companyDetail': companyDetails, 'testDetails': testDetails, 'criteriaDetails': criteriaDetails})


def editDrive(request, id):
    companyDetails = Company.objects.filter(id=id)
    testDetails = Test.objects.filter(id=id)
    criteriaDetails = Criteria.objects.filter(id=id)
    return render(request, "Drives/DriveDetails.html", {'companyDetail': companyDetails, 'testDetails': testDetails, 'criteriaDetails': criteriaDetails})





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
