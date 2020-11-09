from django.urls import path, include
from . import views

urlpatterns = [
    path('drives', views.Drives, name="drives"),
    # path('addDrive', views.Add_Drive, name="addDrive"),

    path('postDrive', views.Post_Drive, name="postDrive"),
    path('driveYear', views.Drive_Year, name="driveYear"),
    path('companyList/<int:year>', views.Company_List, name="companyList"),
    path('driveDetails<int:id>', views.Drive_Details, name="driveDetails"),

]
