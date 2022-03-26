from django.contrib.auth.mixins import LoginRequiredMixin
from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import AddProductForm
from product.models import Brand,Product
from order.models import Cart
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import View


class productListView(ListView):
    model = Product
    template_name = "admin_temp/product_list.html"

class AddproductView(CreateView):
    from_class = AddProductForm
    fields = ['brand_name','product_name', 'product_price','product_image',]
    queryset = Product.objects.all()
  
    success_url = reverse_lazy('products:product_add')
    template_name = "admin_temp/product_add.html"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def form_valid(self, form):
        messages.success(self.request,f"Your Product Added  succesfully")
        return super().form_valid(form)

### Ajax #######################################################

# class CreateproductUser(View):
#     from_class = AddProductForm
#     fields = ['brand_name','product_name', 'product_price','product_image',]
#     queryset = Product.objects.all()
#     queryset = Brand.objects.all()
  
#     success_url = reverse_lazy('products:product_add')
#     template_name = "admin_temp/product_add.html"
#     def  get(self, request):
#         brand_name = request.GET.get('brand_name', None)
#         product_name = request.GET.get('product_name', None)
#         product_price = request.GET.get('product_price', None)
#         product_image = request.GET.get('product_image', None)

#         obj = Product.objects.create(
#             brand_name = brand_name,
#             product_name = product_name,
#             product_price = product_price,
#             product_image = product_image

#         )

#         product = {'id':obj.id,'id':obj.brand_name_id.id,'brand_name':obj.brand_name,'product_name':obj.product_name,'product_price':obj.product_price,'product_image':obj.product_image}

#         data = {
#             'product': product
#         }
        

#         return JsonResponse(data)

        

    

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['brand_name','product_name', 'product_price','product_image', ]
    template_name = "admin_temp/product_update.html"
    success_url = reverse_lazy('products:product_list')


    def form_valid(self, form):
        messages.success(self.request,f"Your Product Update  succesfully")
        return super().form_valid(form)

   
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "admin_temp/product_delete.html"
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        messages.success(self.request,f"Your Product Delete  succesfully")
        return super().form_valid(form)

#####..................Brand Part...............###############################################################


class BrandListView(ListView):
    model = Brand
    template_name = "admin_temp/brand_list.html"

class AddBrandView(CreateView):
    from_class = AddProductForm
    fields = ['brand_name',]
    queryset = Brand.objects.all()
    success_url = reverse_lazy('products:brand_list')
    template_name = "admin_temp/brand_add.html"

   
    
    def form_valid(self, form):
        messages.success(self.request,f"Your Brand Added  succesfully")
        return super().form_valid(form)   
  
class BrandUpdateView(UpdateView):
    model = Brand
    fields = ['brand_name',]
    template_name = "admin_temp/brand_update.html"
    success_url = reverse_lazy('products:brand_list')


    def form_valid(self, form):
        messages.success(self.request,f"Your Brand Update  succesfully")
        return super().form_valid(form)

class BrandDeleteView(LoginRequiredMixin,View):
    def get(self, request,pk):
        user = request.user
        brand = Brand.objects.get(pk=self.kwargs['pk'])
        if brand:
            brand.delete()        
            messages.success(request, 'Brand has been delete!')
        return redirect('products:brand_list')     

        


   
