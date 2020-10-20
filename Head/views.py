from django.shortcuts import render,redirect,reverse

# Create your views here.


def D_Head(request):  # Drive Head Html Page.
    return render(request, "Drives/DriveHead.html")
