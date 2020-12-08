from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Student.models import *
from Drives.models import *
from django.http import HttpResponse
from .forms import PostDrive, PostTest, PostCriteria
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def Drives(request):  # Drive Head Html Page.
    return render(request, "Drives/driveBase.html")


@login_required(login_url='login')
def Student_Drives(request):  # all Stundents drive Html Page.
    drives = Company.objects.all()
    return render(request, "Drives/AllStudentDrives.html", {'drives': drives})


@login_required(login_url='login')
def MyDrives(request):  # all Stundents drive Html Page.
    mydrives = drive.objects.filter(username=request.user)
    return render(request, "Drives/MyDrives.html",{'mydrives': mydrives} )


@login_required(login_url='login')
def StudentDriveBase(request):  # Base drive Stundent Html Page.
    return render(request, "Drives/studentDriveBase.html")


# new drive
@login_required(login_url='login')
def Post_Drive(request):  # posting new Drive
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
            studList = []
            kids = {}
            studentmarks = Academic_table.objects.all()
            for marks in studentmarks:
                if marks.username not in studList:
                    studList.append(marks.username)
            for q in studList:
                total = Academic_table.objects.filter(username=q).order_by('yearOfPass')
                for i in total:
                    kids[i.qualification] = i.CGPA
                count=0
                for key,value in kids.items():
                    if key == '10':
                        if value >= c.SSLC :
                            count = count+1
                    elif key == '12':
                        if value >= c.PUC:
                            count = count+1
                    elif key == 'UG':
                        if value >= c.UG:
                            count = count+1
                    else:
                        if value >= c.PG:
                            count = count+1
                if count == 4:
                    drive.objects.create(username=q,Company_Name=a)
            messages.success(request, 'New Drive Posted ')
            return redirect(Drives)            
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


@login_required(login_url='login')
def Drive_Details(request, id):# get the drive static details
    companyDetails = Company.objects.filter(id=id)
    testDetails = Test.objects.filter(Company_Name=id)
    criteriaDetails=Criteria.objects.filter(Company_Name=id)
    alldrive = drive.objects.filter(username=request.user,Company_Name=id)
    return render(request, "Drives/ViewDrive.html", {'companyDetail': companyDetails, 'testDetails': testDetails, 'criteriaDetails': criteriaDetails, "alldrive": alldrive})


@login_required(login_url='login')
def editDrive(request, id):#get the drive editing page
    companyDetails = Company.objects.filter(id=id)
    testDetails = Test.objects.filter(Company_Name=id)
    criteriaDetails = Criteria.objects.filter(Company_Name=id)
    return render(request, "Drives/DriveDetails.html", {'companyDetail': companyDetails, 'testDetails': testDetails, 'criteriaDetails': criteriaDetails})


@login_required(login_url='login')
def updateDrive(request, id):# save edited Drive details
    if request.method == "POST":
        x = Company.objects.get(id=id)
        y = Test.objects.get(Company_Name=id)
        z = Criteria.objects.get(Company_Name=id)
        form1 = PostDrive(request.POST, instance=x)
        form2 = PostTest(request.POST, instance=y)
        form3 = PostCriteria(request.POST, instance=z)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            a=form1.save()
            b = form2.save(commit=False)
            c = form3.save(commit=False)
            b.Company_Name = a
            b.save()
            c.Company_Name = a
            c.save()
            return redirect(Drive_Details,id)
        else:
            messages.warning(request, 'Please Insert Date.')
            return redirect(editDrive, id)
    else:
        return render(request, "Drives/companyList.html")
    

@login_required(login_url='login')
def AppliedStudents(request, id):  # Applied students list Html Page.
    appliedList = drive.objects.filter(Company_Name=id)
    return render(request, "Drives/AppliedList.html", {'appliedList': appliedList})

@login_required(login_url='login')
def AppliedListUpdate(request,id,d):
    if d == 0:
        drive.objects.filter(id=id).update(Selected_status=3)
    elif d == 1:
        drive.objects.filter(id=id).update(Selected_status=4)
    else:
        pass
    appliedList = drive.objects.filter(id=id)
    return render(request, "Drives/AppliedList.html", {'appliedList': appliedList})


@login_required(login_url='login')
def ApplyReject(request, id,d):
    if d == 1:
        drive.objects.filter(id=id).update(Selected_status=1)
        messages.success(request, 'Applied')
    elif d == 2:
        drive.objects.filter(id=id).update(Selected_status=2)
        messages.warning(request, 'Rejected')
    else:
        pass
    return redirect(MyDrives)
    
