from django.shortcuts import render, redirect, reverse

# Create your views here.


def D_Student(request):  # Drive Stundent Html Page.
    return render(request, "Drives/DriveStudent.html")


def Profile(request):  # Stundent profile Html Page.
    return render(request, "Student/profile.html")
