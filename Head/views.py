from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Student.models import *
from django.http import HttpResponse
from django.contrib import auth
from django.http import JsonResponse
# Create your views here.


@login_required(login_url='login')
def Students(request):
    return render(request, "Student/studentBase.html")

@login_required(login_url='login')
def Batch(request):
    year = Student_Profile.objects.values('batch').distinct()
    return render(request, "Student/studentBatch.html", {'year':year})


@login_required(login_url='login')
def Students_List(request,batch):
    students = Student_Profile.objects.filter(batch=batch)
    return render(request, "Student/studentsList.html", {'students':students,'batch':batch})

@login_required(login_url='login')
def Students_Details(request,id):
    students = User.objects.filter(id = id)
    profile = Student_Profile.objects.filter(username = id)
    academic = Academic_table.objects.filter(username = id)
    skill = skills.objects.filter(username = id)
    project = projects.objects.filter(username = id)
    return render(request, "Student/studentDetails.html",{'students':students,'profile':profile,
                                                    'skill':skill,'project':project,
                                                    'academic':academic
                                                } 
                )


@login_required(login_url='login')
def Update_Student_Profile(request):
    profile = Student_Profile.objects.filter(id = request.POST['id']).update(editStatus=request.POST['editStatus'])
    data = {
        'profile':profile,
    }
    return JsonResponse(data)
    
def addStudentForm(request):
    return render(request, "Admin/addStudent.html")

def addStudent(request):
    if request.method == 'POST':
        
        username=request.POST['username']
        password=request.POST['password']
        if not User.objects.filter(username=username):
            
            user=User.objects.create_user(
                username=username, password=password)
            user.save()
            #JsonResponse({"student":student})
            data = {
                'student':username,
                'password':password,
            }
            return JsonResponse(data)
        else:
            
            #JsonResponse({"username":kid.username})
            data = {
                'username':username,
            }
            return JsonResponse(data)
    return render(request, "Admin/addStudent.html")
