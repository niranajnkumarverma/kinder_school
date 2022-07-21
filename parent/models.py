from django.db import models
from django.utils import timezone
from home.models import User
from datetime import datetime, timedelta
# Create your models here.

occupation_categories = (
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



class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    prof_image = models.FileField(upload_to="parent/profile_img/", default="") 
    father_name = models.CharField(max_length=100, default='')   
    mother_name = models.CharField(max_length=100, default='') 
    occupation = models.CharField(max_length=300,choices=occupation_categories, default='')  
    blood_group = models.CharField(max_length=5, choices=blood_group_choice,default='')  
    gender = models.CharField(max_length=50, choices=gender_choice, default='') 
    dob = models.DateTimeField(blank=True, null=True)
    mobile = models.CharField(max_length=13, default='')   
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)




    class Meta:
        db_table = 'parent'

    def __str__(self):
        return self.user.username 
