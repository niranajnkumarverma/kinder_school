import random

from django.db import models
from home.models import User
from datetime import date, datetime
from django.utils import timezone
import math

from django.contrib.auth.models import PermissionsMixin

from student.models import City, Country,State






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


class Principal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    prof_image = models.FileField(upload_to="principal/profile_img/", default="")   
    father_name = models.CharField(max_length=100, default='')   
    mother_name = models.CharField(max_length=100, default='')   
    dob = models.DateTimeField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, choices=blood_group_choice,blank=True)
    religion = models.CharField(max_length=15,choices=religion_categories_choices,default='' )
    mobile = models.CharField(max_length=10, default='')
    gender = models.CharField(max_length=50, choices=gender_choice,default='')
    address = models.TextField(max_length=50, default='')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,blank=True, default='')
    state = models.ForeignKey(State, on_delete=models.SET_NULL,null=True,blank=True, default='')
    city = models.ForeignKey(City, on_delete=models.SET_NULL,null=True,blank=True, default='')
    pincode = models.CharField(max_length=6, default='')  
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        db_table = 'principal'

  
    def __str__(self):
        return self.first_name  
