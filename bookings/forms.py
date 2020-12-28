from django import forms
from bookings.models import USER_INFO
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password','email')

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = USER_INFO
         fields = ('phone','profile_pic')