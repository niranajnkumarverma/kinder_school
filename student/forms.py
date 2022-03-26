from django import forms
from student.models import Profile
from home.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','mobile','gender','address','country','state','city','pincode']
        
class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ('username', 'password')    