from django import forms
from home.models import Image, Teacher, Video
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.db import transaction
from home.models import User,Teacher,Principal,Staff,Admin
from django.contrib.auth.forms import UserCreationForm



class AdminLoginForm(forms.ModelForm):
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Username'
        }
    ))
    password = forms.CharField(label='Password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Password'
        }
    ))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

    class Meta:
        model = User
        fields = ['username', 'password']

     

class PrincipalSignUpForm(UserCreationForm):
    username = forms.CharField(label='Username*', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Username',
            'pattern': "[a-z]{1,15}",
            'title': "Username should only contain lowercase letters. e.g. niranjan"
        }

    ))
    email = forms.EmailField(label='Email*', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'example@gmail.com',

        }
    ))
    password1 = forms.CharField(label='Password*', required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'

        }
    ))
    password2 = forms.CharField(label='Confirm Password*', required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Confirm password'
        }
    ))

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
           raise ValidationError("This email address is already in use.")
       return self.cleaned_data

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        @transaction.atomic
        def save(self):
            user = super().save(commit=False)
            user.email=self.cleaned_data.get('email')
            user.is_principal = True
            user.save()
            principal = Principal.objects.create(user=user)
            return user





       


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Username*', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Username'
        }
    ))
    password = forms.CharField(label='Password*', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Password'
        }
    ))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

    class Meta:
        model = User
        fields = ['username', 'password']

     


class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile",]

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["name", "school_image",]


class UpdateImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["name", "school_image",]