
from student.models import Profile
from django.db import models
from home.models import User
# Create your models here.
class Publisher(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE, related_name="Publications", null=True)
    publisher_name = models.CharField(max_length=100, null=False)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.publisher_name

class Author(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE, related_name="author",null=True)
    author_name = models.CharField(max_length=250, unique=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.author_name

class Book(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE,  related_name="books",null=True)
    publisher_name=models.ForeignKey(Publisher ,on_delete=models.CASCADE,default="publisher")
    author_name = models.ForeignKey(Author,on_delete=models.CASCADE, default="author")
    book_description = models.TextField(max_length=100)
    book_name = models.CharField(max_length=100)
    book_price = models.IntegerField()
    book_image = models.ImageField(upload_to="school/Books/",null=False, default="default.png")
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,null=True)


    class meta:
        db_table = "book"

    def __str__(self):
        return f"{self.book_name}- {self.publisher_name}"    

   

