from django.shortcuts import render,redirect,reverse

def index(request):
    return render(request, "Student/index.html")
    
def login(request):
    return render(request, "Student/login.html")
    