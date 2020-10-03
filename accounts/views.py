from django.shortcuts import render
from .models import Profile
from .forms import UserForm , ProfileForm
# Create your views here.

def signup():
    pass


def profile():
    pass



def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm()
        profile_form = ProfileForm()
    
    else:
        user_form = UserForm()
        profile_form = ProfileForm()       

    return render(request,'profile/profile_edit.html',{
        'user_form' : user_form , 
        'profile_form' : profile_form
    })