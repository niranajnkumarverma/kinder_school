from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from admin_portal.students.forms import AddUserForm, StudentListForm
from django.views.generic import ListView,CreateView,UpdateView,View
from django.urls import reverse_lazy
from home.models import User
from django.contrib import messages
from student.models import Student

class StudentsView(LoginRequiredMixin,ListView):
    model = Student
    success_url = reverse_lazy('students:students')
    template_name = "admin_temp/student_list.html"


    

class AddUserView(LoginRequiredMixin,CreateView):
    from_class = AddUserForm
    fields = ['publisher_name','book_name', 'book_price','book_image',]
    queryset = User.objects.all()  
    success_url = reverse_lazy('products:product_add')
    template_name = "admin_temp/product_add.html"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def form_valid(self, form):
        messages.success(self.request,f"Your Product Added  succesfully")
        return super().form_valid(form)
    

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    fields = ['brand_name','product_name', 'product_price','product_image', ]
    template_name = "admin_temp/product_update.html"
    success_url = reverse_lazy('products:product_list')


    def form_valid(self, form):
        messages.success(self.request,f"Your Product Update  succesfully")
        return super().form_valid(form)

   


class UserDeleteView(LoginRequiredMixin,View):
    queryset = User.objects.all()

    def get(self, request,pk):
        user = request.user
        user = User.objects.get(pk=self.kwargs['pk'])
        if user:
            user.delete()        
            messages.success(request, 'User has been delete!')
        return redirect('students:students')     
 

   
   
        


   
