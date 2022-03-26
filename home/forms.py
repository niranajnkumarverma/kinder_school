from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label= 'Enter your Username',widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Enter Username'
        }
    ))
    # first_name = forms.CharField(label= 'Enter your first name', widget = forms.TextInput(
    #     attrs = {
    #         'class':'form-control',
    #         'placeholder':'first name'
    #     }
    # ))

    # last_name = forms.CharField(label= 'Enter your Last name', widget = forms.TextInput(
    #     attrs = {
    #         'class':'form-control',
    #         'placeholder':'last name'
    #     }
    # ))
   
    email = forms.EmailField(label= 'Enter your valid  Email', widget = forms.EmailInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Enter your email'
        }
    ))
    password1 = forms.CharField(label= 'Enter your password',widget=forms.PasswordInput(
       attrs = {
            'class':'form-control',
            'placeholder':'Enter your password'
        }
    ))  
    # password2 = forms.CharField(label= 'Enter your confirm password',widget=forms.PasswordInput(
    #    attrs = {
    #         'class':'form-control',
    #         'placeholder':'Enter your Confirm password'
    #     }
    # ))  
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email','password1', )
        

     


