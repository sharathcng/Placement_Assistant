from django.urls import path, include
from . import views

urlpatterns = [
    path('drives', views.Drives, name="drives"),
    # path('addDrive', views.Add_Drive, name="addDrive"),
    path('studentDriveBase', views.StudentDriveBase, name="studentDriveBase"),
    path('student_drives', views.Student_Drives, name="student_drives"),
    path('mydrives', views.MyDrives, name="mydrives"),
    path('AppliedStudents<int:id>', views.AppliedStudents, name="AppliedStudents"),
    path('listUpdate<int:id><int:d>',
         views.AppliedListUpdate, name="listUpdate"),

    path('postDrive', views.Post_Drive,
         name="postDrive"),  # posting new drive
    path('driveYear', views.Drive_Year, name="driveYear"),
    path('companyList/<int:year>', views.Company_List, name="companyList"),
    path('editDrive<int:id>', views.editDrive, name="editDrive"),
    path('updateDrive<int:id>', views.updateDrive, name="updateDrive"),
    path('driveDetails<int:id>', views.Drive_Details, name="driveDetails"),

]
