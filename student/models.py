
import random
from django.core.management.base import BaseCommand, CommandError
from django.db import models
from home.models import User
from datetime import datetime, timedelta
from django.utils import timezone
from datetime import date
from django.db.models.functions import Now



class Command(models.Manager):   
    def get_queryset(self):
        User._base_manager.filter(created_at__lte=datetime.now()-timedelta(days=1)).delete()
      
   
  
       











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



section_categories = (
    ('None', 'Select Section'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F')

)


country_categories = (
    ('None', 'Select Country'),
    ('i', 'India'),
    ('c', 'China'),
    ('u', 'United States'),
    ('i', 'Indonesia'),
    ('p', 'Pakistan'),
    ('b', 'Brazil'),
    ('b', 'Bangladesh'),
    ('r', 'Russia'),
    ('j', 'Japan'),
    ('u', 'United Kingdom'),
    ('i', 'Iran'),
    ('f', 'France'),
    ('s', 'South Korea'),
    ('c', 'Canada'),
    ('t', 'Thailand'),
    ('g', 'Germany'),
    ('t', 'Turkey'),
    ('t', 'Tanzania'),
    ('m', 'Mexico')
)


state_categories = (
    ('None', 'Select Country'),
    ('i', 'Andhra Pradesh	'),
    ('c', 'Arunachal Pradesh'),
    ('u', 'Assam '),
    ('i', 'Bihar'),
    ('p', 'Chhattisgarh'),
    ('b', 'Goa'),
    ('b', 'Gujarat'),
    ('r', 'Haryana'),
    ('j', 'Himachal Pradesh'),
    ('u', 'Jharkhand'),
    ('i', 'Karnataka'),
    ('f', 'Kerala'),
    ('s', 'Madhya Pradesh'),
    ('c', 'Maharashtra'),
    ('t', 'Manipur'),
    ('g', 'Meghalaya'),
    ('t', 'Mizoram'),
    ('t', 'Nagaland'),
    ('m', 'Odisha'),
    ('m', 'Punjab'),
    ('m', 'Rajasthan'),
    ('m', 'Sikkim'),
    ('m', 'Tamil Nadu'),
    ('m', 'Telangana'),
    ('m', 'Tripura'),
    ('m', 'Uttar Pradesh'),
    ('m', 'Uttarakhand'),
    ('m', 'West Bengal')

)

city_categories = (
    ('None', 'Select City'),
    ('Mumbai', 'Mumbai'),
    ('d', 'Delhi'),
    ('b', 'Bengaluru '),
    ('h', 'Hyderabad'),
    ('a', 'Ahmedabad'),
    ('c', 'Chennai'),
    ('k', 'Kolkata'),
    ('s', 'Surat'),
    ('p', 'Pune'),
    ('k', 'Kanpur'),
    ('j', 'Jaipur'),
    ('n', 'Navi Mumbai'),
    ('l', 'Lucknow'),
    ('n', 'Nagpur'),
    ('c', 'Coimbatore'),
    ('i', 'Indore'),
    ('v', 'Vadodara'),
    ('k', 'Kallakurichi'),
    ('p', 'Patna'),
    ('b', 'Bhopal	'),
    ('l', 'Ludhiana'),
    ('m', 'Madurai'),
    ('t', 'Tirunelveli'),
    ('a', 'Agra'),
    ('r', 'Rajkot'),
    ('n', 'Najafgarh'),
    ('j', 'Jamshedpur'),
    ('g', 'Gorakhpur'),
    ('n', 'Nashik'),
    ('p', 'Pimpri'),
    ('k', 'Kalyan'),
    ('t', 'Thane'),
    ('m', 'Meerut'),
    ('n', 'Nowrangapur'),
    ('f', 'Faridabad'),
    ('g', 'Ghaziabad'),
    ('d', 'Dhanbad'),
    ('d', 'Dombivli'),
    ('v', 'Varanasi'),
    ('r', 'Ranchi'),
    ('a', 'Amritsar'),
    ('a', 'Allahabad'),
    ('v', 'Visakhapatnam'),
    ('t', 'Teni'),
    ('j', 'Jabalpur'),
    ('h', 'Haora'),
    ('t', 'Tiruchirappalli'),
    ('a', 'Aurangabad'),
    ('s', 'Shivaji Nagar'),
    ('s', 'Solapur'),
    ('s', 'Srinagar'),
    ('t', 'Tiruppur'),
    ('c', 'Chandigarh'),
    ('j', 'Jodhpur'),
    ('s', 'Salem'),
    ('g', 'Guwahati'),
    ('g', 'Gwalior'),
    ('v', 'Vijayawada'),
    ('m', 'Mysore'),
    ('r', 'Rohini'),
    ('h', 'Hubli'),
    ('n', 'Narela	'),
    ('j', 'Jalandhar'),
    ('t', 'Thiruvananthapuram'),
    ('k', 'Kota'),
    ('b', 'Bhubaneshwar'),
    ('a', 'Aligarh'),
    ('b', 'Bareilly'),
    ('m', 'Moradabad'),
    ('b', 'Bhiwandi'),
    ('r', 'Raipur'),
    ('b', 'Borivli'),
    ('p', 'Puducherry'),
    ('b', 'Bhilai'),
    ('b', 'Bhavnagar'),
    ('c', 'Cochin'),



)

class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name




       

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    prof_image = models.FileField(upload_to="student/profile_img/", default="")   
    father_name = models.CharField(max_length=100, default='')
    mother_name = models.CharField(max_length=100, default='')
    father_occupation = models.CharField(max_length=300,choices=father_occupation_categories, default='')
    blood_group = models.CharField(max_length=5, choices=blood_group_choice,default='')
    religion = models.CharField(max_length=15,choices=religion_categories_choices, default='' )
    classe = models.CharField(max_length=10, choices=class_categories_choices,default='')
    section = models.CharField(max_length=20, choices=section_categories, default='')
    role = models.CharField(max_length=12, default='')
    dob = models.DateTimeField(blank=True, null=True)
    mobile = models.CharField(max_length=13, default='')
    gender = models.CharField(max_length=50, choices=gender_choice , default='')
    address = models.TextField(max_length=50, default='')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True,blank=True, default='')
    state = models.ForeignKey(State, on_delete=models.SET_NULL,null=True,blank=True, default='')
    city = models.ForeignKey(City, on_delete=models.SET_NULL,null=True,blank=True, default='')
    pincode = models.CharField(max_length=6, default='')      
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)




    class Meta:
        db_table = 'student'

    def __str__(self):
        return str(self.country,self.state,self.city)

   
 




class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time_st = models.DateTimeField(auto_now=True)
	otp = models.SmallIntegerField()


class Code(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    number = models.CharField(max_length=5, blank=True)
  

    def __str__(self):
        return str(self.number)

    def save(self,*args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []
        for i in range(5):
            num  = random.choice(number_list)
            code_items.append(num)
        code_string = "".join(str(item) for item in code_items)
        self.number = code_string    
        super().save(*args,**kwargs)

