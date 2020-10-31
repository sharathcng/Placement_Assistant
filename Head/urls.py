from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('D_Head', views.D_Head, name="D_Head"),
    path('CompanyDetails', views.Companydetails, name="CompanyDetails"),
    path('TestDetails', views.Testdetails, name="TestDetails"),
    path('CriteriaDetails', views.Criteriadetails, name="CriteriaDetails"),
]
