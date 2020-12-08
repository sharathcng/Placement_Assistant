from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Student.models import *
from Drives.models import drive,Company
from django.http import JsonResponse
from .forms import updatePics,updateMarks

# Create your views here.



def Profile(request):  # Stundent profile Html Page.
    users = User.objects.filter(username = request.user)
    profile = Student_Profile.objects.filter(username = request.user)
    academic = Academic_table.objects.filter(username = request.user)
    skill = skills.objects.filter(username = request.user)
    project = projects.objects.filter(username = request.user)
    context = {'users': users, 'profile': profile,
               'skill': skill, 'project': project,
               'academic': academic
               }
    for student in users:
        if student.first_name == '':
            return render(request, "Student/profileEdit.html",{'profilepic':profile})
        for profile in profile:
            if profile.editStatus == 0 or profile.editStatus == 2:
                return render(request, "Student/profileEdit.html",{'profilepic':profile})
            else:
                return render(request, "Student/profile.html",context )
    #return render(request, "Student/profile.html",context )
    
@login_required(login_url='login')
def edit_profile(request):
    return render(request, "Student/profileEdit.html")


def updatePic(request):
    if request.method == "POST":
        form = updatePics(request.POST,request.FILES)
        if  form.is_valid():
            m = Student_Profile.objects.get(username=request.user)
            m.profilepic = form.cleaned_data['profilepic']
            m.save()
    return redirect(Profile)

def updateMark(request):
    if request.method == "POST":
        form = updateMarks(request.POST,request.FILES)
        if  form.is_valid():
            return redirect(Profile)
            # m = Academic_table.objects.get(username=request.user)
            # m.markscard = form.cleaned_data['markscard']
            # m.save()
    return redirect(Profile)

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
            CGPA=request.POST['cgpa'],
            qualification=request.POST['qualification']
            )

    # academic = {'courses':user.courses, 'college':user.college, 'university':user.university,'yearofPass':user.yearofPass,'cgpa':user.cgpa}
    data = {
        'user':user,
    }
    return JsonResponse(data)
    
def update_skill(request):
    user = skills.objects.filter(username=request.user).update_or_create(
            username=request.user,
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
    student_2 = Student_Profile.objects.update_or_create(username=request.user,
            defaults = {
            'dateOfBirth' : request.POST['date'],
            'gender' : request.POST['gender'],
            'phoneNumber' : request.POST['phoneNumber'],
            'courseName' : request.POST['courseName'],
            'semester' : request.POST['semester'],
            'bloodGroup' : request.POST['bloodGroup'],
            'batch' : request.POST['batch'],
            # 'profilepic' : request.FILES['profilepic']
            }
            )

    data = {
        'student_1':student_1,
        'student_2':list(student_2.values()),
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
