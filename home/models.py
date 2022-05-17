from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime
from django.contrib.auth.models import PermissionsMixin

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)                                       
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
   
                                   


    
gender_choice = (
    ('m', 'Male'),
    ('f', 'Female')
)


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


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.FileField(upload_to="admin/profile_img/", default="default.png")
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    dob = models.DateTimeField(blank=True, default='', null=True,)
    blood_group = models.CharField(max_length=5, choices=blood_group_choice,blank=True)
    religion = models.CharField(max_length=15,choices=religion_categories_choices,default='Hindu' )
    mobile = models.CharField(max_length=10, default='')
    gender = models.CharField(max_length=50, choices=gender_choice, blank=True)
    address = models.TextField(max_length=50, default='')
    country = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    pincode = models.CharField(max_length=6, default='')    


    class Meta:
        db_table = 'admin'

    def __str__(self):
        return 'No Details' if not self.first_name else self.last_name


class Principal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.FileField(upload_to="principal/profile_img/", default="default.png")
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    dob = models.DateTimeField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, choices=blood_group_choice,blank=True)
    religion = models.CharField(max_length=15,choices=religion_categories_choices,default='Hindu' )
    mobile = models.CharField(max_length=10, default='')
    gender = models.CharField(max_length=50, choices=gender_choice,default='')
    address = models.TextField(max_length=50, default='')
    country = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    pincode = models.CharField(max_length=6, default='')  

    class Meta:
        db_table = 'principal'

  
    def __str__(self):
        return self.first_name  



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.FileField(upload_to="teacher/profile_img/", default="default.png")
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    classe = models.CharField(max_length=10, choices=class_categories_choices,default='Nursery')
    section = models.CharField(max_length=20, choices=section_categories_choices, default='A')
    dob = models.DateTimeField(blank=True,null=True)
    blood_group = models.CharField(max_length=5, choices=blood_group_choice,default='A+')
    religion = models.CharField(max_length=15,choices=religion_categories_choices, default='hindu' )
    mobile = models.CharField(max_length=10, default='')
    gender = models.CharField(max_length=50, choices=gender_choice, default='male')
    address = models.TextField(max_length=50, default='')
    country = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    pincode = models.CharField(max_length=6, default='')  

    class Meta:
        db_table = 'teacher'
  

    def __str__(self):
        return str(self.user)  


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.FileField(upload_to="student/profile_img/", default="default.png")
    fullName = models.CharField(max_length=50, default='')
    father_name = models.CharField(max_length=100, default='')
    mother_name = models.CharField(max_length=100, default='')
    father_occupation = models.CharField(max_length=100 , default='')
    blood_group = models.CharField(max_length=5, choices=blood_group_choice,default='A+')
    religion = models.CharField(max_length=15,choices=religion_categories_choices, default='hindu' )
    classe = models.CharField(max_length=10, choices=class_categories_choices,default='nursery')
    section = models.CharField(max_length=20, choices=section_categories_choices, default='A')
    role = models.CharField(max_length=12,blank=True)
    dob = models.DateTimeField(blank=True, null=True)
    mobile = models.CharField(max_length=10, default='')
    gender = models.CharField(max_length=50, choices=gender_choice , default='male')
    address = models.TextField(max_length=50, default='')
    country = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    pincode = models.CharField(max_length=6, default='')  


    class Meta:
        db_table = 'student'

   

    def __str__(self):
        return self.fullName  


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.FileField(upload_to="staff/profile_img/", default="default.png")
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    dob = models.DateTimeField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, choices=blood_group_choice,default='A+')
    religion = models.CharField(max_length=15,choices=religion_categories_choices ,default='hindu')
    mobile = models.CharField(max_length=10, default='')
    gender = models.CharField(max_length=50, choices=gender_choice, default='male')
    address = models.TextField(max_length=50, default='')
    country = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    pincode = models.CharField(max_length=6, default='')  

    class Meta:
        db_table = 'staff'

   

    def __str__(self):
        return self.first_name  


## .....................Video part ........................................##

class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(
        upload_to='school_video', null=True, verbose_name="")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name + ": " + str(self.videofile)


class Image(models.Model):
    name = models.CharField(max_length=500)
    school_image = models.ImageField(upload_to="school_pics")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name + ": " + str(self.school_image)
