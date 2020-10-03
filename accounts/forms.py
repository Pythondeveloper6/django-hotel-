from django import forms
from . models import Profile
from django.contrib.auth.models import User




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','phone_number','address']