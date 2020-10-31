from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Student.models import Student_Profile
from django.contrib.auth.models import AnonymousUser

# Create your views here.
def index(request):
    return render(request, "index.html")
    
def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_superuser is True:
                auth.login(request, user)
                return redirect(admin_home)
            else:
                auth.login(request, user)
                return redirect(home)
        else:
            return render(request,'Student/login.html',{'usernameError':"Username doesnot exist"})
    else:
        return render(request,'Student/login.html')


def logout(request):
    auth.logout(request)
    return redirect(index)

@login_required
def home(request):
    return render(request, "Student/home.html")
    
@login_required
def admin_home(request):
    return render(request, "Admin/home.html")
    