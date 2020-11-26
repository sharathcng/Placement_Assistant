from django.urls import path, include
from . import views

urlpatterns = [
    path('drives', views.Drives, name="drives"),
    # path('addDrive', views.Add_Drive, name="addDrive"),

    path('postDrive', views.Post_Drive,
         name="postDrive"),  # posting new drive
    path('driveYear', views.Drive_Year, name="driveYear"),
    path('companyList/<int:year>', views.Company_List, name="companyList"),
    path('editDrive<int:id>', views.editDrive, name="editDrive"),
    path('updateDrive<int:id>', views.updateDrive, name="updateDrive"),
    path('driveDetails<int:id>', views.Drive_Details, name="driveDetails"),

]
