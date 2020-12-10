from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Student.models import *
from Drives.models import drive,Company
from django.http import JsonResponse
from django.db.models import Sum



def report(request):  # Drive Stundent Html Page.
    year = Company.objects.values('Year').distinct()
    #print(year)
    # a = year[0]
    # b = year[1]
    #print(a['Year'],b['Year'])
    years = []
    # for y in year :
    #     i = y['Year']
    #     years.append(i)
    #     years.append(Company.objects.filter(Year=y['Year']).count())
    # print(years)
    for y in year :
        #print(y['Year'])
        z = str(y['Year'])
        years.append([z,Company.objects.filter(Year=y['Year']).count()])
    
    select = drive.objects.values('Company_Name').distinct()
    selected = []
    for s in select :
        #print(y['Year'])
        z = str(s['Company_Name'])
        selected.append([z,drive.objects.filter(Company_Name=s['Company_Name'],Selected_status=3).count()])
    print(selected)
    # selected = drive.objects.values(
    #             'Company_Name').annotate(Sum('Company_Name'))


    return render(request, "Reports/reportHome.html",{'years':years,'selected':selected})


# def bookir_chart(request):
#     labels = []
#     data = []
#     qury = Company.objects.values('Year').distinct()
#     dept2 = Company.objects.values(
#         'Company_Name').annotate(Sum('Company_Name'))
#     for entry in dept2:
#         data.append(entry['Company_Name'])
#     for val in qury:
#       labels.append(val['Year'])
#     data = {
#         'labels': labels,
#         'data': data
#     }
#     return JsonResponse(data)
