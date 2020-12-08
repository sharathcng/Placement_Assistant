from django.shortcuts import render,redirect,reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Student.models import *
from Drives.models import drive,Company
from django.http import JsonResponse

# Create your views here.


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
    #print(years)

    # l = []
    # for j in years:
    #     print(years.keys())
    #     for b in range(len(years)):
    #         l[b]+=years.keys[b]
    #         l[b]+=years.values[b]
    # print(l)
    return render(request, "Reports/reportHome.html",{'years':years})


# def bookir_chart1(request):
#     labels = []
#     data = []
#     qury = Company.objects.values("Year")
#     dept1 = Company.objects.values(
#         'Company_Name').annotate(Sum('Company_Name'))
#     for entry in dept1:
#         data.append(entry['Company_Name__sum'])
#     for val in qury:
#         labels.append(val['Company_Name'])
#     data = {
#         'labels': labels,
#         'data': data
#     }
#     return JsonResponse(data)
