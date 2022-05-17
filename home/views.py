
from django import forms
from django.template import RequestContext
from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from home.forms import LoginForm, StudentSignUpForm
from order.models import Cart
from home.models import Image, User, Video
from django.views.generic.base import View
from django.views.generic import RedirectView
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from home.forms import LoginForm
from django.contrib.auth.views import LoginView 
from django.views.generic.edit import FormView 
from django.contrib.auth import login 
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin



def index(request):
    signup_form = StudentSignUpForm()  
    login_form = LoginForm()  
    video = Video.objects.all() 
    image =  Image.objects.all()
    cart = Cart.objects.filter()
    context = {"signup_form": signup_form, "login_form": login_form,'video':video,'image':image,'cart_data':{'total_cart': len(cart)}}   
    return render(request, 'user/index.html', context)


# @login_required
def signup(request):
    signup_form = StudentSignUpForm()
    login_form = LoginForm()  
    if request.method == 'POST':
        signup_form = StudentSignUpForm(request.POST)
        if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created!!'+ username)
                return redirect('index')  
        # messages.error(request, "Unsuccessful registration. Invalid information.")                     
    return render(request, 'user/index.html', {'signup_form': signup_form ,"login_form": login_form})

def login_view(request):
    signup_form = StudentSignUpForm()
    login_form = LoginForm(request.POST or None)
    if request.POST and login_form.is_valid():
        user = login_form.login(request)
        if user.is_student:
            login(request, user)
            messages.success(request,"You are Login Succesfully!!")
            return redirect("student:student_profile")      
    return render(request, 'user/index.html', {'login_form': login_form ,'signup_form': signup_form })

   

# class UserLogin(SuccessMessageMixin, LoginView):
#     from_class = LoginForm
#     success_url = reverse_lazy('student:student_profile')
#     template_name = 'user/index.html' 

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)   
#         login_form = LoginForm()
#         signup_form = SignUpForm()
#         context = {'login_form':login_form,'signup_form': signup_form }
#         return context
      
#     def form_valid(self,form):
#         messages.success(self.request,"You are Login Succesfully!!")
#         return super().form_valid(form)


# class IndexView(TemplateView):
#     template_name = 'user/index.html' 
   
#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)   
       
#         context['login_form'] =self.login_form 
#         context['signup_form'] =self.signup_form
#         context['signup_action'] = reverse("signup")
#         return context

    
   

# class SignUpView(CreateView):
#     model = User
#     fields = ['username', 'email', 'password1', 'password2']
#     signup_form = StudentSignUpForm
#     success_url = reverse_lazy("index")
#     template_name = 'user/index.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)   

   
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('index')

     


    
   
#     def form_valid(self, form):
#         if request.method == 'POST':
#             form = SignUpForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(self.request,f"Account create succesfully")
#         else:
#             form = SignUpForm()              
#         return super().form_valid(form)    

#     def form_invalid(self, form):

#         # here, how do I pass form.errors back to the home_page?
#         # I know messages framework is possible but this isn't as
#         # easy to add each error to its respective field as 
#         # form.errors would be.

#         return HttpResponseRedirect(reverse('index'))



#     # def get_context_data(self, **kwargs):
#     #     context =  super().get_context_data(**kwargs)   
#     #     video = Video.objects.all() 
#     #     context['video'] = video
#     #     image =  Image.objects.all()
#     #     context['image'] =image
#     #     cart = Cart.objects.filter()[::-1]
       
#     #     context['cart_data'] = {'total_cart': len(cart)}
#     #     return context






  

class TeacherView(TemplateView):
    template_name = 'user/teacher.html' 

class ContactView(TemplateView):
    template_name = 'user/contact.html'  

class AboutView(TemplateView):
    template_name = 'user/about.html'        

class GalleryView(TemplateView):
    template_name = 'user/gallery.html' 

class CourseView(TemplateView):
    template_name = 'user/course.html'



class EventView(TemplateView):
    template_name = 'user/event.html'               

class LogoutView(RedirectView):
    url = '/'
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)