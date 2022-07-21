from random import choices
from django import forms
from superadmin.models import  Address, AdminProfileModel, Image, Logo, Title, Video
from principal.models import Principal
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.db import transaction
from home.models import User
from django.contrib.auth.forms import UserCreationForm
from student.models import Code, Student, User,State,City,Country
from django.forms import ModelForm


WEEKDAYS = (
  ('Monday',"Monday"),
  ('Tuesday',"Tuesday"),
  ('Wednesday',"Wednesday"),
  ('Thursday',"Thursday"),
  ('Friday',"Friday"),
  ('Saturday',"Saturday"),
  ('Sunday',"Sunday"),
)


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


class_categories = {
    'Select Class': [],
    'Play': [],
    'Nursery': [],
    'One': [],
    'Two': [],
    'Three': [],
    'Four': [],
    'Five': [],
    'Six': [],
    'Seven': [],
    'Eight': [],
    'Nine': [],
    'Tenth': [],
    'Eleven': []
}

class_categories_choices = []
for c in class_categories.keys():
    class_categories_choices.append((c, c.capitalize()))
class_categories_choices = tuple(class_categories_choices)


section_categories = (
    ('None', 'Select Section'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F')

)

class Logoform(forms.ModelForm):
    class Meta:
        model= Logo
        fields= ['site_logo']


class Titleform(forms.ModelForm):
    site_title = forms.CharField(label='Site Title', required=True, widget=forms.TextInput(
        attrs={
           
            'class': 'form-control',
            'placeholder': 'Enter Site title',

        }
    ))
    class Meta:
        model= Title
        fields= ['site_title']

class Addressform(forms.ModelForm):
    apartment_name = forms.CharField(label='Apartment Name', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter aparment name',

        }
    ))
    floor_no = forms.CharField(label='Floor Number', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter floor no',

        }
    ))
    site_address = forms.CharField(label='Site Address', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter site address',

        }
    ))
    toll_free_no = forms.CharField(label='Toll Free Number', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter toll.free.no',

        }
    ))
    alt_toll_free_no = forms.CharField(label='Alt Toll Free number', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter toll.free.no',

        }
    ))
    pincode = forms.IntegerField(label='pincode number', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter pincode',

        }
    ))
    site_email = forms.EmailField(label='Email ', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter email',

        }
    ))
    weekday = forms.ChoiceField(label='Weakday ', choices=WEEKDAYS)

    from_hour = forms.TimeField(
        label='Start',
        widget=forms.widgets.TimeInput(attrs={'type':'time'}),
    )
    to_hour = forms.TimeField(
        label='End',
        widget=forms.widgets.TimeInput(attrs={'type':'time'}),
    )
         

    class Meta:
        model= Address
        fields= ['apartment_name','floor_no', 'site_address','toll_free_no','alt_toll_free_no','pincode','site_email', 'weekday','from_hour','to_hour']
      
     

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

     

class AdminProfile(forms.ModelForm):
    # prof_image = forms.FileField(label='Profile Image', required=True, widget=forms.FileInput(

    #     attrs={
    #         'class': 'form-control',

    #     }

    # ))
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
        model = AdminProfileModel
        fields = ['father_name', 'mother_name', 'dob', 'blood_group','religion', 'mobile', 'gender', 'address', 'country', 'state', 'city', 'pincode', ]
        widgets = {
            'dob': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }



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


class CountryCsvImportForm(forms.ModelForm):
    csv_upload = forms.FileField()

    class Meta:
        model = Country
        fields = '__all__'


class StateCsvImportForm(forms.ModelForm):
    country_id = forms.IntegerField(
       
    )
    csv_upload = forms.FileField()

   
    class Meta:
        model = State
        fields = '__all__'



class CityCsvImportForm(forms.ModelForm):
    csv_upload = forms.FileField()
   
    class Meta:
        model = City
        fields = '__all__'   


       
   
  
  
