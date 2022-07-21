
from django.core.exceptions import ValidationError
from django.db import transaction
from home.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from security.models import Security
from student.models import City,State


gender_choice = (

    ('Male', 'Male'),
    ('Female', 'Female')
)


blood_group_choice = (
    ('None', 'Select Blood Group'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),

    ('O+', 'O+'),
    ('O-', 'O-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-')
)


religion_categories = {
    'Select Religion': [],
    'Hindu': [],
    'Islam': [],
    'Christian': [],
    'Buddish': [],
    'Others': []
}
religion_categories_choices = []
for r in religion_categories.keys():
    religion_categories_choices.append((r, r.capitalize()))
Product_categories_choices = tuple(religion_categories_choices)


father_occupation_categories = (
    (None, 'Select Occupation'),
    ('Managers', 'Managers'),
    ('Professional', 'Professional'),
    ('Technicians and associate professionals.',
     'Technicians and associate professionals.'),
    ('Clerical support workers.', 'Clerical support workers.'),
    ('Service and sales workers.', 'Service and sales workers.'),
    ('Skilled agricultural, forestry and fishery workers.',
     'Skilled agricultural, forestry and fishery workers.'),
    ('Plant and machine operators, and assemblers.',
     'Plant and machine operators, and assemblers.'),
    ('Government and Public Administration.',
     'Government and Public Administration.'),
    ('Agriculture, Food and Natural Resources. Architecture and Construction',
     'Agriculture, Food and Natural Resources. Architecture and Construction'),
    ('Business and financial operations: Cost analyst',
     'Business and financial operations: Cost analyst'),
    ('Law: Paralegal.', 'Law: Paralegal.'),
    ('Hospitality and Tourism', 'Hospitality and Tourism'),
    ('Manufacturing', 'Manufacturing')
)


class UserDeactivateForm(forms.Form):
    deactivate = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserDeactivateForm, self).__init__(*args, **kwargs)
        self.fields['deactivate'].help_text = "Check this box if you are sure you want to delete account."

    def clean_is_active(self):

        is_active = not(self.cleaned_data["deactivate"])
        return is_active


class UserDeleteForm(forms.Form):
    """
    Simple form that provides a checkbox that signals deletion.
    """
    delete = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserDeleteForm, self).__init__(*args, **kwargs)
        self.fields['delete'].help_text = "Check this box if you are sure you want to delete this account."


class SecuritySignUpForm(UserCreationForm):
    username = forms.CharField(label='Username*', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Username',

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
        user.email = self.cleaned_data.get('email')
        user.is_security = True
        user.save()
        security = Security.objects.create(user=user)
        return user


class SecurityProfileForm(forms.ModelForm):
    prof_image = forms.FileField(label='Profile Image', required=True, widget=forms.FileInput(

        attrs={
            'class': 'form-control',

        }

    ))
    father_name = forms.CharField(label='Father Name', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Father name',

        }
    ))
    mother_name = forms.CharField(label='Mother Name', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Mother Name',

        }
    ))

    father_occupation = forms.ChoiceField(
        label='Father Occupation', choices=father_occupation_categories)

    blood_group = forms.ChoiceField(
        label='Blood Group', choices=blood_group_choice)

    religion = forms.ChoiceField(
        label='Religion', choices=religion_categories_choices)

    mobile = forms.CharField(label='Mobile Number', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your phone number',
        }
    ))
    gender = forms.ChoiceField(label='Gender', choices=gender_choice)

    address = forms.CharField(label='Address', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Address',
        }
    ))

    pincode = forms.CharField(label='Pincode', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Pincode',
        }
    ))

    class Meta():
        model = Security
        fields = ['prof_image', 'father_name', 'mother_name', 'father_occupation', 'dob', 'blood_group',
                  'religion', 'mobile', 'gender', 'address', 'country', 'state', 'city', 'pincode', ]
        widgets = {
            'dob': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(
                    country_id=country_id).order_by('name')

            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk and self.instance.country:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(
                    state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty District queryset
        elif self.instance.pk and self.instance.state:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')        
 
            
