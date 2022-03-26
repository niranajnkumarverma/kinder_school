from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


## .....................Video part ........................................##

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='school_video', null=True, verbose_name="")
   

    def __str__(self):
        return self.name + ": " + str(self.videofile)

class Image(models.Model):
    name= models.CharField(max_length=500)
    schoolimage = models.ImageField( upload_to="school_pics")

    def __str__(self):
        return self.name + ": " + str(self.schoolimage)        


