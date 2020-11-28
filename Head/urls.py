from django.urls import path, include
from . import views

urlpatterns = [
    
    path('Students', views.Students, name = "Students"),
    path('batch', views.Batch, name = "batch"),
    path('studentsList/<int:batch>', views.Students_List, name="studentsList"),
    path('studentDetails/<int:id>', views.Students_Details, name = "studentDetails"),
    path('updateStudentProfile', views.Update_Student_Profile, name = "updateStudentProfile"),
    path('addStudentForm', views.addStudentForm, name = "addStudentForm"),
    path('addStudent', views.addStudent, name = "addStudent"),
    path('resetpassword', views.ResetPassword, name="resetpassword"),
    

]
