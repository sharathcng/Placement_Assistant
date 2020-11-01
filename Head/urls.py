from django.urls import path, include
from . import views

urlpatterns = [
    
    path('Students', views.Students, name = "Students"),
    path('studentsList/<int:batch>', views.Students_List, name="studentsList"),
    path('studentDetails/<int:id>', views.Students_Details, name = "studentDetails"),
    
]
