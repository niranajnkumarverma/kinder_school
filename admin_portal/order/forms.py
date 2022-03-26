from django import forms
from order.models import Order
from product.models import Product

class AddProductForm(forms.ModelForm):
    
    class Meta():
        model = Product
        fields = ['product_name', 'product_price','product_image', ]
        

class OrderstatusForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = ['status',]     


