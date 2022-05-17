from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.db import transaction
from home.models import Student, User,Teacher
from django.contrib.auth.forms import UserCreationForm
from django import forms


blood_group_choice = (
    ('a+', 'A+'),
    ('a-', 'A-'),
    ('b+', 'B+'),
    ('b-', 'B-'),
    ('b+', 'B+'),
    ('o+', 'O+'),
    ('o-', 'O-'),
    ('ab+', 'AB+'),
    ('ab-', 'AB-')
)



religion_categories = {
    'Hindu': [],
    'Islam': [],
    'Christian': [],
    'Buddish': [],
    'Others': []
}
religion_categories_choices = []
for r in religion_categories.keys():
    religion_categories_choices.append( (r, r.capitalize()) )
Product_categories_choices = tuple(religion_categories_choices)


class_categories = {
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
    'Eleven':[]
}

class_categories_choices = []
for c in class_categories.keys():
    class_categories_choices.append( (c, c.capitalize()) )
class_categories_choices = tuple(class_categories_choices)


section_categories = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': []
   
}
section_categories_choices = []
for s in section_categories.keys():
    section_categories_choices.append( (s, s.capitalize()) )

section_categories_choices = tuple(section_categories_choices)


    
gender_choice = (
    ('m', 'Male'),
    ('f', 'Female')
)


class TeacherSignUpForm(UserCreationForm):
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
        user.email=self.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        return user



class TeacherProfile(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter First Name',
        }
    ))
    last_name = forms.CharField(label='Last Name', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Last Name',
        }
    ))

    classe = forms.ChoiceField(label='Class', choices=class_categories_choices)

    section = forms.ChoiceField(label='Section', choices=section_categories_choices)


    dob = forms.DateField(label='Date of Birth',widget=forms.DateInput(format='%d/%m/%Y'))

    blood_group = forms.ChoiceField(label='Blood Group', choices=blood_group_choice)

      
    religion = forms.ChoiceField(label='Religion', choices=religion_categories_choices)

      
    mobile = forms.CharField(label='Mobile Number', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your phone number',
        }
    ))
    gender = forms.ChoiceField(label='Gender',choices=gender_choice)

      
    address = forms.CharField(label='Address', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Address',
        }
    ))
    country = forms.CharField(label='Country', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your country',
        }
    ))
    state = forms.CharField(label='State', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your State',
        }
    ))
    city = forms.CharField(label='City', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your city',
        }
    ))
    pincode = forms.CharField(label='Pincode', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Your Pincode',
        }
    ))
    image = forms.FileField(label='Image', required=True)


    class Meta():
        model = Student
        fields = ['first_name', 'last_name', 'classe', 'section','dob', 'blood_group','religion','mobile','gender', 'address', 'country','state', 'city','pincode','image']
        # widgets = {
        #     'dob': forms.DateInput(attrs={'type':'date'}),
        #     'address':forms.Textarea(attrs={'cols':10,'rows':3})
        # }

