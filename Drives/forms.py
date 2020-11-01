from django import forms
from Head.models import Company,Criteria,Test


class CompanyForms(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        exclude = ['Date']
        
    # def __init__(self, *args, **kwargs):
    #     super(CompanyForms, self).__init__(*args, **kwargs)
    #     # self.fields['email'].required = False


class TestForms(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(TestForms, self).__init__(*args, **kwargs)
    #     # self.fields['email'].required = False


class CriteriaForms(forms.ModelForm):
    class Meta:
        model = Criteria
        fields="__all__"
        

    # def __init__(self, *args, **kwargs):
    #     super(CriteriaForms, self).__init__(*args, **kwargs)
    #     # self.fields['email'].required = False
