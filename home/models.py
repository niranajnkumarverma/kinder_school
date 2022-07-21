
import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime,timedelta
from django.utils import timezone



class User(AbstractUser):
    is_superuser = models.BooleanField(default=False)  
    is_principal = models.BooleanField(default=False)                                       
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    is_security = models.BooleanField(default=False)


   

class Contact(models.Model):
    fullname = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message  =models.TextField(max_length=200)

    class Meta:
        db_table = 'contact'

   

    def __str__(self):
        return str(self.fullname,self.subject)






