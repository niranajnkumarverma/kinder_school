from django.db import models
from home.models import User
from product.models import Book
from student.models import Student

# Create your models here.


class Cart(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    quantity=models.CharField(max_length=10, default="1")
    price = models.CharField(max_length=10, default="0")
    total = models.CharField(max_length=10, default="0")
    

    def save(self, *args, **kwargs):
        if self.price and self.quantity:
            self.total = int(self.price) * int(self.quantity)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}- {self.book.book_name} -- {self.book.book_price}"  


orderstatus = (
    ('pending' , 'pending'),
    ('Out For Shipping' , 'Out For Shipping'),
    ('Completed' , 'Completeted'),
) 

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    profile = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.FloatField(null=True)
    transaction_id = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=150, choices=orderstatus, default='pending' )
    tracking_no = models.CharField(max_length=150, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True )

   
     
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    price = models.CharField(max_length=10, default="0")
    total = models.CharField(max_length=10, default="0")

    def save(self, *args, **kwargs):
        if self.price and self.quantity:
            self.total = int(self.price) * int(self.quantity)
        return super().save(*args, **kwargs)   
  

    def __str__(self):
        return '{} - {}'.format(self.order.id , self.order.tracting_no)
       
 

class Transaction(models.Model):
    made_by = models.CharField(max_length=100)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)          
     
