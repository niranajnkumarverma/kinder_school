from datetime import date
from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from django.views.generic import View
from django import views
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from order.models import Cart
from product.models import Book,Publisher

from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from superadmin.models import Address, FooterBackground, HeaderBackground, Logo, Title
# Create your views here.

   
class ShopView(ListView):
    model = Book
    template_name = 'user/shop.html'  
    success_url = reverse_lazy('product:shopview')  

    def get_queryset(self):
        publisher_name = self.request.GET.get('publisher',None)
        queryset =  super().get_queryset()
        if publisher_name:
            queryset= queryset.filter(publisher_name=publisher_name)
        print("<<<<<<<<<<<<<",publisher_name)    
        print(type(queryset))
        print(queryset.query)    
        return queryset    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        publishers = Publisher.objects.all()
        books = Book.objects.all()
        site_logo = Logo.objects.all().first()
        site_title = Title.objects.all().first()
        site_address = Address.objects.all().first() 
        header = HeaderBackground.objects.all().first()
        footer = FooterBackground.objects.all().first()        
        cart = Cart.objects.filter(user=self.request.user)[::-1]
        # for  brand in brands:
        #     brands.count = Brand.objects.filter(brand = brand).count()
        context = {'site_title':site_title,'site_logo':site_logo,'footer':footer,'header':header,'site_address':site_address,'publishers':publishers, 'books':books, 'cart_data':{'total_cart': len(cart)}}
        return context

  








