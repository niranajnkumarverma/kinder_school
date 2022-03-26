from venv import create
from django.db import models
from django.contrib.auth.models import User
from home.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

gender_choice = (
    ('m', 'Male'),
    ('f', 'Female'),
)
               
# STATES = (
#     ('', 'Choose...'),
#     ('JH', 'Jharkhand'),
#     ('BR', 'Bihar'),
#     ('GUJ', 'Gujrat')
# )


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    image = models.ImageField( upload_to="profile_pics")
    mobile = models.CharField(max_length=10, unique=True,default='')
    gender = models.CharField(max_length=50, choices=gender_choice)
    address = models.CharField(max_length=50,default='')
    country = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user.username} Profile"


    # @receiver(post_save, sender = User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user = instance)
    # @receiver(post_save, sender=User)            

    # def save_user_profile(sender , instance,  **kwargs):
    #     instance.profile.save()



