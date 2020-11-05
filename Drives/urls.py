from django.urls import path, include
from . import views

urlpatterns = [
    path('drives', views.Drives, name="drives"),
    # path('addDrive', views.Add_Drive, name="addDrive"),
    # path('TestDetails', views.Testdetails, name="TestDetails"),
    # path('CriteriaDetails', views.Criteriadetails, name="CriteriaDetails"),

    path('postDrive', views.Post_Drive, name="postDrive"),
    # path('postTest', views.Post_Test, name="postTest"),
    # path('postCriteria', views.Post_Criteria, name="postCriteria")

]