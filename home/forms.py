from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.contrib.auth.forms import PasswordResetForm


class ContactForm(forms.ModelForm):
    fullname = forms.CharField(label='Fullname', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your fullname',

        }
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your email address',

        }
    ))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Subject',

        }
    ))
    message = forms.CharField(label='Message', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your message',

        }
    ))

    class Meta:
        model = Contact
        fields = ['fullname', 'email', 'subject', 'message', ]


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
