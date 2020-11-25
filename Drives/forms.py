from django import forms
from Drives.models import Company,Criteria,Test


class PostCompany(forms.ModelForm):
    class Meta:
        model = Company
        fields="__all__"
        exclude = ('Status','Year',)

    def _init_(self, *args, **kwargs):
        super(PostDrive, self)._init_(*args, **kwargs)
        self.fields['stipend'].required = False

class PostTest(forms.ModelForm):
    class Meta:
        model = Test
        fields="__all__"
        exclude = ('Company_Name',)

    def _init_(self, *args, **kwargs):
        super(PostTest, self)._init_(*args, **kwargs)
        

class PostCriteria(forms.ModelForm):
    class Meta:
        model = Criteria
        fields="__all__"
        exclude = ('Company_Name',)

    def _init_(self, *args, **kwargs):
        super(PostCriteria, self)._init_(*args, **kwargs)
