
from student.models import Profile
from django.db import models
from home.models import User
# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=100, null=True, blank=True)
    date=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.brand_name

class Product(models.Model):
    brand_name=models.ForeignKey(Brand ,on_delete=models.CASCADE,default="brand")
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField( null=True, blank=True)
    product_image = models.ImageField(upload_to="seller/products/", default="default.png")
    date=models.DateTimeField(auto_now_add=True,null=True)


    class meta:
        db_table = "product"

    def __str__(self):
        return f"{self.product_name}- {self.brand_name}"    

   

