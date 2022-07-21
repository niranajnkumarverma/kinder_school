
from django.contrib.auth.decorators import login_required
from dataclasses import dataclass
import os
from urllib import response
from django import http
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic import View
from django import views
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from student.forms import StudentProfileForm, UserDeactivateForm, UserDeleteForm
from django.contrib.auth.views import LoginView  
from home.models import  User
from order.models import Cart
from django.views.generic.base import View
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from student.models import Student,State,City,Country
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template.loader import get_template
from superadmin.models import Address, FooterBackground, HeaderBackground, Logo, Title
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders




class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'user/student_prof.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Student.objects.filter(user=self.request.user)
        cart = Cart.objects.filter(user=self.request.user)[::-1] 
        account_delete_form = UserDeleteForm()
        deactivate_form = UserDeactivateForm()
        site_logo = Logo.objects.all().first()
        site_title = Title.objects.all().first()
        site_address = Address.objects.all().first() 
        header = HeaderBackground.objects.all().first()
        footer = FooterBackground.objects.all().first()   
        context = {'site_title':site_title,'site_logo':site_logo,'footer':footer,'header':header,'site_address':site_address,'deactivate_form':deactivate_form, 'account_delete_form':account_delete_form    ,'profile':profile,'cart_data':{'total_cart': len(cart)}}
        return context

class UserDeactivateView(LoginRequiredMixin, View):
    """
    Deactivates the currently signed-in user by setting is_active to False.
    """
    def get(self, request, *args, **kwargs):
        deactivate_form = UserDeactivateForm()
        return render(request, 'user/student_prof.html', {'deactivate_form': deactivate_form})

    def post(self, request, *args, **kwargs):
        deactivate_form = UserDeactivateForm(request.POST)
        if deactivate_form.is_valid():           
            request.user.is_active = False
            request.user.save()           
            logout(request)         
            messages.success(request, 'Account successfully deactivated')           
            return redirect(reverse('index'))
        return render(request, 'user/student_prof.html', {'deactivate_form': deactivate_form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """
    def get(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm()
        return render(request, 'user/user_deletion.html', {'account_delete_form': account_delete_form})

    def post(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm(request.POST)      
        if account_delete_form.is_valid():
            user = request.user          
            logout(request)          
            user.delete()
            messages.success(request, 'Account successfully deleted')
            return redirect(reverse('index'))
        return render(request, 'user/student_prof.html', {'account_delete_form': account_delete_form})




# def delete_profile(request):
#     user = User.objects.filter(id = request.user.profile.user_id)
#     try:
#         user.delete()
#     except:
#         messages.error(request,'Please try again.')
#         return redirect('profile')

#     messages.success(request, 'Profile successfully deleted.')
#     return redirect('index')


def student_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    student  = get_object_or_404(Student,pk=pk)
    template_path = 'user/user_printer.html'
    context = {'student': student}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="student_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response







# AJAX
def load_state(request):    
    country_id = request.GET.get('country_id')    
    state = State.objects.filter(country_id=country_id).all()
    return render(request, 'user/city_dropdown_list_options.html', {'state': state})


def load_cities(request):   
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()   
    return render(request, 'user/city_dropdown_list_options.html', {'cities':cities})


class StudentProfile(LoginRequiredMixin,TemplateView):
    from_class = StudentProfileForm
    template_name = 'user/profile_update.html'
    success_url = reverse_lazy('student_profile')

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        student_profile_form = Student.objects.get_or_create(user=self.request.user)
        student_profile_form = StudentProfileForm(post_data, file_data, instance=request.user.student)
       
        if student_profile_form.is_valid():
           
            student_profile_form.save()
            messages.success(request, 'Your profile Update  succesfully!')
            return redirect('student:student_profile')

        context = self.get_context_data(
        site_logo = Logo.objects.all().first(),
        site_title = Title.objects.all().first(),
        site_address = Address.objects.all().first() ,
        header = HeaderBackground.objects.all().first(),
        footer = FooterBackground.objects.all().first() ,      
        
            student_profile_form=student_profile_form

        )   
        return self.render_to_response(context)

    def get(self, request,  *args , **kwargs):
        return self.post(request, *args, **kwargs)  

       




def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(),content_type  = "applicxation/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404         

  

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/student_prof.html'
    success_url = reverse_lazy('student:student_profile')

    def form_valid(self,form):
        messages.success(self.request, 'Your Password changed  succesfully!')
        return super().form_valid(form)




# Change user profile edit form design 
# set  user user upload image display  left side on edit page

# create download pdf from user profile imformation 

# setup pdf template view display on table form data

# create  link for user direct click on print button 
#           create  link for user direct click on print button then load print pages