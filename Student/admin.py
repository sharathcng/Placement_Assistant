from django.contrib import admin
from .models import Student_Profile

# Register your models here.
@admin.register(Student_Profile)
class Student_Profile_Admin(admin.ModelAdmin):
    list_display = ('username', 'dateOfBirth', 'gender','bloodGroup','course','semester',
                    'phoneNumber','hobbies','knownLanguages','currentAddress','permanentAddress'
                    )
    list_filter = ('gender', 'bloodGroup', 'semester')
    search_fields = ('username','hobbies')
    date_hierarchy = 'dateOfBirth'
    ordering = ('username','dateOfBirth')