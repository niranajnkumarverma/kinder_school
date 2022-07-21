from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from superadmin.models import Address, FooterBackground, HeaderBackground,  Image, Logo, Title, Video
from order.models import Cart
from product.models import Book
from django.views.generic.base import View
from django.views.generic import RedirectView
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from home.forms import ContactForm, LoginForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.core.mail import send_mail
from random import randint
import os
import re
import requests
from home.utils import send_sms
from student.forms import MobileOTPForm, StudentSignUpForm
from teacher.models import Teacher
from django.contrib.auth import get_user_model
User = get_user_model()















app_info = {
    'app_title': 'kinder school',
    'app_name': 'kinder school management',
    'msg_data': {'name': '', 'msg': '', 'type': 'success', 'display': ''},
    'login': 'app/doctor_content.html'
}


def console(err):
    print(err)
    print('Type of error: ', type(err))
    print(err.args)

# check internet connection
def isConnected():
    try:
        url = requests.get('http://google.com', timeout=3)
        status = url.status_code
        if status:
            return True
    except Exception as err:
        app_info['msg_data']['name'] = 'Internet Not Available'
        app_info['msg_data']['msg'] = 'Check your internet connection.'
        return False





def index(request):
    signup_form = StudentSignUpForm()
    login_form = LoginForm()
    video = Video.objects.all()
    image = Image.objects.all()
    site_logo = Logo.objects.all().first()
    site_title = Title.objects.all().first()
    site_address = Address.objects.all().first()
    cart = Cart.objects.filter()
    header = HeaderBackground.objects.all().first()
    footer = FooterBackground.objects.all().first()
    app_info['msg_data']['display'] = 'hide'
   
    context = {'header':header, 'footer':footer,'site_title':site_title,'site_address':site_address,'site_logo':site_logo,"signup_form": signup_form,"login_form": login_form,'app_info':app_info,
               'video': video, 'image': image, 'cart_data': {'total_cart': len(cart)}}
    return render(request, 'user/index.html', context)


def signup(request):
    signup_form = StudentSignUpForm()
    login_form = LoginForm()
    if request.method == 'POST': 
        signup_form = StudentSignUpForm(request.POST)
        if signup_form.is_valid():
            user=signup_form.save() 
            username = signup_form.cleaned_data.get('username') 
            email = signup_form.cleaned_data.get('email')   
            # user.is_active =  False
            user.save()
            request.session['email'] = email   
            request.session['username'] = username 
            on_success = send_otp(request)
            print('success: ', on_success)            
            if on_success:
                messages.success(
                request, f'One-Time Password has sent to {email}')              
                return redirect(otp_page) 
            else:
                return redirect(index)
    return render(request, 'user/index.html', {'signup_form': signup_form, "login_form": login_form})            





def send_otp(request, otp_for='reg'):
    app_info['verify_for'] = otp_for
    email_to_list = [request.session['email'],]
    subject = 'Welcome to kinder school - Verify Your Email'
    otp = randint(1000,9999)
    print('OTP is: ', otp)
    request.session['otp'] = otp
    message = f"Your one time otp for Kinder school  Register  is: {otp}"
    # print("1111111111111",message)
    email_from = settings.EMAIL_HOST_USER
    # print("2222222222",email_from)
    try:
        if isConnected():
            send_mail(subject, message, email_from, email_to_list)
            return True
        return False
    except settings.EMAIL_AUTH_ERROR as err:
        link = '((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)'
        get_link = re.findall(link, err.args[1].decode('utf8'))[0][0]
        print('Email Error: ', get_link)
        return False

# otp page
def otp_page(request):
    # print('Verify for: ', app_info['verify_for'])

    return render(request,'user/otp.html', app_info)


# otp verify functionality
def verify_otp(request, verify_for='reg'):
    if request.method == 'POST':
       
        if int(request.POST['otp']) == request.session['otp']:  
            user = request.session['email']        
            messages.success(request, f'Your account has been created!!')
            del request.session['otp']
            del request.session['email']

            return redirect(index)
        else:
            app_info['msg_data']['name'] = 'Invalid OTP'
            app_info['msg_data']['msg'] = "OTP does not matched. Please enter correct otp."
            app_info['msg_data']['type'] = 'warning'
            app_info['msg_data']['display'] = 'show'
            return redirect(otp_page)
    else:
        app_info['msg_data']['name'] = 'Invalid Request'
        app_info['msg_data']['msg'] = "Something went wrong. Please try again leter."
        app_info['msg_data']['type'] = 'warning'
        app_info['msg_data']['display'] = 'show'
        return redirect(otp_page)


def resend_otp(request):
    email = request.POST.get('email')
    username = request.POST.get('username')
    if request.method == 'GET':            
            print("33333333333333333",email)  
            request.session['email'] = email 
            print("22222222222222222",email)  
            request.session['username'] = username        
            on_success = send_otp(request)
            print('success: ', on_success)            
            if on_success:
                messages.success(
                request, f'One-Time Password has Resent to {email}')              
                return redirect(otp_page) 
            else:
                return redirect(index)
    return render(request,'user/otp.html', app_info)
	

@csrf_exempt
def login_view(request):
    signup_form = StudentSignUpForm()
    login_form = LoginForm(request.POST or None)

   
    if request.POST and login_form.is_valid():
        # if user is not None:
        #     request.session['pk'] = user.pk   
        #     return redirect('verify-view')     
        user = login_form.login(request)
       
        clientkey = request.POST["g-recaptcha-response"]
        secretkey = "6LcxoBAgAAAAAG9_h2ioAxvBKwaJep3eGDShMit6"
        captchaData = {
            'secret': secretkey,
            'response': clientkey
        }
        r = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print("your secret is", verify)  
       
        if verify:
            messages.success(request, "You are Login Succesfully!!")

            # return HttpResponse('<script>alert("success");</script>')
        else:
            messages.error(request, "Invalid captcha")
            # return HttpResponse('<script>alert("not success");</script>')
            return redirect("index")
         
        if user.is_student:
            request.session['pk'] = user.pk  #### This is call twilio mobile otp verification 
            login(request, user)
            return redirect('verify-view')  
        else:
            return redirect("home:admin_login")
        # return redirect("student:student_profile")
    return render(request, 'user/index.html', {'login_form': login_form, 'signup_form': signup_form})


def verify_view(request):
    mobile_otp_form = MobileOTPForm(request.POST or None)
    pk = request.session.get('pk')
    print("..................", pk)

    if pk:
        user = User.objects.get(pk=pk)
        print("..................", user)
        code = user.code
        print("..................", code)
        code_user = f"{user.username}:{user.code}"
        if not request.POST:
            print(code_user)
            send_sms(code_user, user.student.mobile)

        if mobile_otp_form.is_valid():
            num = mobile_otp_form.cleaned_data.get('number')
            if str(code) == num:
                code.save()
                return redirect("index")
            else:
                return redirect('verify-view')
    return render(request, 'user/mobile_otp_verify.html', {'mobile_otp_form': mobile_otp_form})


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            fullname = contact_form.cleaned_data.get('fullname')
            messages.success(request, f'Your message has been Send!!' + fullname)
            return redirect('contactview') 
    site_logo = Logo.objects.all().first()
    site_title = Title.objects.all().first()        
    header = HeaderBackground.objects.all().first()
    footer = FooterBackground.objects.all().first()
    site_address = Address.objects.all().first()             
    return render(request, 'user/contact.html',{'contact_form': contact_form, 'header':header, 'footer':footer, 'site_address':site_address, 'site_logo':site_logo, 'site_title':site_title})




class AboutView(TemplateView):
    template_name = 'user/about.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        site_logo = Logo.objects.all().first()
        site_title = Title.objects.all().first()
        site_address = Address.objects.all().first()  
        header = HeaderBackground.objects.all().first()
        footer = FooterBackground.objects.all().first()
        context = {'header':header, 'footer':footer, 'site_address':site_address, 'site_logo':site_logo, 'site_title':site_title}
        

        return context


class GalleryView(TemplateView):
    template_name = 'user/gallery.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        site_logo = Logo.objects.all().first()
        site_title = Title.objects.all().first()
        site_address = Address.objects.all().first()  
        header = HeaderBackground.objects.all().first()
        footer = FooterBackground.objects.all().first()
        context = {'header':header, 'footer':footer,'site_address':site_address, 'site_logo':site_logo, 'site_title':site_title}
        

        return context


class CourseView(TemplateView):
    template_name = 'user/course.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        site_logo = Logo.objects.all().first()
        site_title = Title.objects.all().first()
        courses = Book.objects.all()
        site_address = Address.objects.all().first()  
        header = HeaderBackground.objects.all().first()
        footer = FooterBackground.objects.all().first()
        context = {'header':header, 'footer':footer,'courses':courses,'site_address':site_address, 'site_logo':site_logo, 'site_title':site_title}
        
    
        return context




class TeacherView(TemplateView):
    template_name = 'user/teacher.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        site_logo = Logo.objects.all().first()
        site_title = Title.objects.all().first()
        teacher = Teacher.objects.all()
        site_address = Address.objects.all().first()  
        header = HeaderBackground.objects.all().first()
        footer = FooterBackground.objects.all().first()
        context = {'header':header, 'footer':footer,'teacher':teacher,'site_address':site_address,'site_logo':site_logo, 'site_title':site_title}
        

        return context

   

class EventView(TemplateView):
    template_name = 'user/event.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        site_logo = Logo.objects.all().first()
        site_title = Title.objects.all().first()
        events = Image.objects.all()
        site_address = Address.objects.all().first()  
        header = HeaderBackground.objects.all().first()
        footer = FooterBackground.objects.all().first()
        context = {'header':header, 'footer':footer,'events':events,'site_address':site_address, 'site_logo':site_logo, 'site_title':site_title}
        
    
        return context


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
