from django import forms
from Notifications.models import Notifications


# class PostNotification(forms.ModelForm):
#     class Meta:
#         model = Notifications
#         fields="__all__"
#         exclude = ('view_Status',)

#     def _init_(self, *args, **kwargs):
#         super(PostNotification, self)._init_(*args, **kwargs)
#         self.fields['username'] = 'request.user'