from django.contrib.auth.mixins import LoginRequiredMixin
from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
import order
from student.forms import ProfileForm


from student.models import Profile
from .forms import AddProductForm, OrderstatusForm
from product.models import Product
from order.models import Cart, Order, OrderItem, Transaction
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages


class CartListView(ListView):
    model = Cart
    template_name = "admin_temp/cart_list.html"


class OrderListView(ListView):
    model = Order
    template_name = "admin_temp/order_list.html"
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter()
        context['transaction_id'] = Transaction.objects.filter()
        return context

class OrderUpdateView(UpdateView):
    from_class = OrderstatusForm
    fields = ['status',]
    model = Order
    template_name = "admin_temp/order_update.html"
    success_url = reverse_lazy('orders:order_list')
    

    def form_valid(self, form):
        messages.success(self.request,f"Your order status update  succesfully")
        return super().form_valid(form)
   
class OrderDeleteView(View):
    def get(self, request,pk):
        user = request.user
        order = Order.objects.get(pk=self.kwargs['pk'])
        if order:
            order.delete()        
            messages.success(request, 'order has been delete!')
        return redirect('orders:order_list')     

        


class OrderDetailView(View):

    def get(self, request):
        user = request.user
        orderitem = OrderItem.objects.all()
        order_amount = Order.objects.filter(user=user.pk)
        order_address = Profile.objects.filter(user=user.pk)   
        context = {'orderitem':orderitem,'order_address':order_address, 'order_amount':order_amount}

        return render(request, 'admin_temp/order_detail.html', context)
    # template_name = "admin_temp/order_detail.html"


    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context['orderitem'] = OrderItem.objects.all()
    #     context['order_address'] = Profile.objects.filter()
       
    #     context['amout'] = Order.objects.all()
    #     return context



   


    
   



   
  
   
        


   
