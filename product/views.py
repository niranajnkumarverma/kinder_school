from datetime import date
from itertools import product
from multiprocessing import context
from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.views.generic import View
from django import views
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from order.models import Cart
from product.models import Brand,Product
from student.models import Profile
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Create your views here.

   
class ShopView(ListView):
    model = Product
    template_name = 'user/shop.html'  
    success_url = reverse_lazy('product:shopview')  

    def get_queryset(self):
        brand_name = self.request.GET.get('brand',None)
        queryset =  super().get_queryset()
        if brand_name:
            queryset= queryset.filter(brand_name=brand_name)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>",brand_name)
        print(type(queryset))
        print(queryset.query)    
        return queryset    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        brands = Brand.objects.all()
        cart = Cart.objects.filter(user=self.request.user)[::-1]
       
        context['cart_data'] = {'total_cart': len(cart)}
        # for  brand in brands:
        #     brands.count = Brand.objects.filter(brand = brand).count()
        context['brands']=brands
        return context

  








