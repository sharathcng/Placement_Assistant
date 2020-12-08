from django import forms
from Student.models import *

class updatePics(forms.ModelForm):
    class Meta:
        model = Student_Profile
        fields=["profilepic"]

    def _init_(self, *args, **kwargs):
        super(updatePics, self)._init_(*args, **kwargs)

class updateMarks(forms.ModelForm):
    class Meta:
        model = Academic_table
        fields=["markscard"]

    def _init_(self, *args, **kwargs):
        super(updateMarks, self)._init_(*args, **kwargs)