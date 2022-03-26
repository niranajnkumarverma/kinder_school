from email.mime import image
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import MyUserCreationForm
from order.models import Cart
from home.models import Image, User, Video
from django.views.generic.base import View
from django.views.generic import RedirectView
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, logout as auth_logout



# Create your views here.
class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('student:login')
    template_name = 'user/index.html'
    
    def form_valid(self, form):
        messages.success(self.request,f"Account create succesfully")
        return super().form_valid(form)

    def is_valid(self, form):
        user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password1'])
        user.save()
        return super(SignUpView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)   
        video = Video.objects.all() 
        context['video'] = video
        image =  Image.objects.all()
        context['image'] =image
        cart = Cart.objects.filter()[::-1]
       
        context['cart_data'] = {'total_cart': len(cart)}
        return context

  

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