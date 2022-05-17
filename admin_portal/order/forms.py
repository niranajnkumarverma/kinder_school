from django import forms
from order.models import Order
from product.models import Book

class AddProductForm(forms.ModelForm):
    
    class Meta():
        model = Book
        fields = ['book_name', 'book_price','book_image', ]
        

class OrderstatusForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = ['status',]     


