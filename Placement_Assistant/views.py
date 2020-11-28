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
            auth.login(request, user)
            return redirect(home)
        else:
            return render(request,'login.html',{'usernameError':"Username doesnot exist"})
    else:
        return render(request,'login.html')


@login_required(login_url='login')
def ChangePassword(request):
    if request.method == 'POST':
        username = request.user
        password = request.POST['OldPassword']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            user.set_password(request.POST['NewPassword'])
            user.save()
        return redirect(index)
    else:
        return render(request, "Student/ChangePassword.html")



def logout(request):
    auth.logout(request)
    return redirect(index)

@login_required
def home(request):
    return render(request, "home.html")
