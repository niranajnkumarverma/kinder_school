from home.models import User
from django.db import models
from student.models import City, Country,State
from colorfield.fields import ColorField

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


class AdminProfileModel(models.Model):
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
        db_table = 'adminprofilemodel'

  

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE )
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    icon_url = models.CharField(max_length=200)
    url  = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)




    def __str__(self):
        return self.title




class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='school_video', null=True, verbose_name="")
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



class Logo(models.Model):
  
    site_logo = models.ImageField(upload_to="site_logo",blank=True, null=True)

class Title(models.Model):
   
    site_title = models.CharField(max_length=100,blank=True, null=True)   


WEEKDAYS = (
  ('Monday',"Monday"),
  ('Tuesday',"Tuesday"),
  ('Wednesday',"Wednesday"),
  ('Thursday',"Thursday"),
  ('Friday',"Friday"),
  ('Saturday',"Saturday"),
  ('Sunday',"Sunday"),
)


class Address(models.Model):
    apartment_name = models.CharField(max_length=100)
    floor_no = models.CharField(max_length=20,blank=True, null=True)
    site_address = models.TextField(blank=True, null=True)
    toll_free_no = models.IntegerField(blank=True, null=True)
    alt_toll_free_no = models.IntegerField(blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    site_email = models.EmailField(blank=True, null=True)
    weekday = models.CharField(max_length=100,choices=WEEKDAYS,blank=True,null=True)
    from_hour = models.TimeField(blank=True,null=True)
    to_hour = models.TimeField(blank=True,null=True)
  
    def __str__(self):
      return str(self.apartment_name,self.floor_no,self.toll_free_no)

    class Meta:
        db_table = 'address'


class HeaderBackground(models.Model):
    color = ColorField(format="hexa")
   

    class Meta:
        db_table = 'headerbackground'
    

class FooterBackground(models.Model):
    color = ColorField(format="hexa")
   

    class Meta:
        db_table = 'footerbackground'
