from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Student.models import *
from Drives.models import *
from django.http import JsonResponse

# Create your views here.


def D_Student(request):  # Drive Stundent Html Page.
    drives = Company.objects.all()
    return render(request, "Drives/DriveStudent.html",{'drives':drives})


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


def Get_details(request):
    student = User.objects.filter(username = request.user)
    academic = Academic_table.objects.filter(username = request.user)
    skill = skills.objects.filter(username = request.user)
    personal = Student_Profile.objects.filter(username = request.user)
    project = projects.objects.filter(username = request.user)
    return JsonResponse({"academic":list(academic.values()),"skill":list(skill.values()),"student":list(student.values()),
                        "personal":list(personal.values()),"project":list(project.values())})




def update_academic(request):
    user = Academic_table.objects.create(
            username=request.user,
            courses=request.POST['course'],
            college=request.POST['institute'],
            university=request.POST['university'],
            yearOfPass=request.POST['yearOfPass'],
            CGPA=request.POST['cgpa']
            )

    # academic = {'courses':user.courses, 'college':user.college, 'university':user.university,'yearofPass':user.yearofPass,'cgpa':user.cgpa}
    data = {
        'user':user,
    }
    return JsonResponse(data)
    
def update_skill(request):
    user = skills.objects.filter(username=request.user).update(
            languages=request.POST['languages'],
            operatingSystem=request.POST['os'],
            database=request.POST['database'],
            technologies=request.POST['tech'],
            applications=request.POST['application']
            )

    data = {
        'user':user,
    }
    return JsonResponse(data)


def update_hobbies(request):
    user = Student_Profile.objects.filter(username=request.user).update(
            hobbies=request.POST['hobbies']
            )

    data = {
        'user':user,
    }
    return JsonResponse(data)


def update_personal(request):
    user = Student_Profile.objects.filter(username=request.user).update(
            knownLanguages=request.POST['languages'],
            permanentAddress=request.POST['permanent'],
            currentAddress=request.POST['current']
            )

    data = {
        'user':user,
    }
    return JsonResponse(data)

def update_project(request):
    user = projects.objects.create(
            username=request.user,
            title=request.POST['title'],
            description=request.POST['description']
            )

    data = {
        'user':user,
    }
    return JsonResponse(data)

def update_profile(request):
    student_1 = User.objects.filter(username=request.user).update(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email']
            )
    student_2 = Student_Profile.objects.filter(username=request.user).update(
            dateOfBirth=request.POST['date'],
            gender=request.POST['gender'],
            phoneNumber=request.POST['phoneNumber']
            )

    data = {
        'student_1':student_1,
        'student_2':student_2
    }
    return JsonResponse(data)






def delete_academic(request):
    Academic_table.objects.filter(id = request.POST['id'], username=request.user ).delete()
    data = {
        'deleted': True
    }
    return JsonResponse(data)

def delete_project(request):
    projects.objects.filter(id = request.POST['id'], username=request.user ).delete()
    data = {
        'deleted': True
    }
    return JsonResponse(data)