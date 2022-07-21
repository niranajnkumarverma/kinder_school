


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







father_occupation_categories = (
    (None,'Select Occupation'),
    ('Managers' ,'Managers'),
    ('Professional','Professional'),
    ('Technicians and associate professionals.','Technicians and associate professionals.'),
    ('Clerical support workers.','Clerical support workers.'),
    ('Service and sales workers.','Service and sales workers.'),
    ('Skilled agricultural, forestry and fishery workers.','Skilled agricultural, forestry and fishery workers.'),
    ('Plant and machine operators, and assemblers.','Plant and machine operators, and assemblers.'),
    ('Government and Public Administration.','Government and Public Administration.') ,
    ('Agriculture, Food and Natural Resources. Architecture and Construction','Agriculture, Food and Natural Resources. Architecture and Construction'),
    ('Business and financial operations: Cost analyst','Business and financial operations: Cost analyst'),
    ('Law: Paralegal.','Law: Paralegal.'),
    ('Hospitality and Tourism','Hospitality and Tourism'),
    ('Manufacturing','Manufacturing')
)



class Security(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    prof_image = models.FileField(upload_to="security/profile_img/", default="")   
    father_name = models.CharField(max_length=100, default='')   
    mother_name = models.CharField(max_length=100, default='')   
    father_occupation = models.CharField(max_length=300,choices=father_occupation_categories, default='')
    dob = models.DateTimeField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, choices=blood_group_choice,default='A+')
    religion = models.CharField(max_length=15,choices=religion_categories_choices ,default='')
    mobile = models.CharField(max_length=10, default='')
    gender = models.CharField(max_length=50, choices=gender_choice, default='')
    address = models.TextField(max_length=50, default='')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,blank=True, default='')
    state = models.ForeignKey(State, on_delete=models.SET_NULL,null=True,blank=True, default='')
    city = models.ForeignKey(City, on_delete=models.SET_NULL,null=True,blank=True, default='')
    pincode = models.CharField(max_length=6, default='') 
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)
   
    class Meta:
        db_table = 'security'

   

    def __str__(self):
        return self.user.username  