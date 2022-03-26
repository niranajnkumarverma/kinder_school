from django import forms
from product.models import Brand, Product

class AddProductForm(forms.ModelForm):
    
    class Meta():
        model = Product
        fields = ['brand_name','product_name', 'product_price','product_image', ]
        

class AddBrandForm(forms.ModelForm):
    
    class Meta():
        model = Brand
        fields = ['brand_name',]
             


