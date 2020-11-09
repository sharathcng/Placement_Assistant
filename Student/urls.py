from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('student_drives', views.Student_Drives, name="student_drives"),

    path('Profile', views.Profile, name="Profile"),
    path('ajax/getDetails', views.Get_details, name="getDetails"),
    path('ajax/updateAcademic', views.update_academic, name="updateAcademic"),
    path('ajax/updateSkill', views.update_skill, name="updateSkill"),
    path('ajax/updateHobbies', views.update_hobbies, name = "updateHobbies"),
    path('ajax/updatePersonal', views.update_personal, name = "updatePersonal"),
    path("ajax/updateProject", views.update_project, name="updateProject"),
    path("ajax/updateProfile", views.update_profile, name="updateProfile"),

    path("ajax/deleteAcademic", views.delete_academic, name="deleteAcademic"),
    path("ajax/deleteProject", views.delete_project, name="deleteProject"),
    
    

]
