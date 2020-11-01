from django.urls import path, include
from . import views

urlpatterns = [
    
    path('Students', views.Students, name = "Students"),
    path('batch', views.Batch, name = "batch"),
    path('studentsList/<int:batch>', views.Students_List, name="studentsList"),
    path('studentDetails/<int:id>', views.Students_Details, name = "studentDetails"),
    
]
