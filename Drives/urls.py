from django.urls import path, include
from . import views

urlpatterns = [
    path('drives', views.Drives, name="drives"),
    path('addDrive', views.Add_Drive, name="addDrive"),
    path('TestDetails', views.Testdetails, name="TestDetails"),
    path('CriteriaDetails', views.Criteriadetails, name="CriteriaDetails"),

]