
from admin_portal.principals.forms import UserDeactivateForm, UserDeleteForm
from admin_portal.securities.forms import SecurityProfileForm, SecuritySignUpForm
from home.models import User
from django import forms
from django.contrib import messages
from security.models import Security
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView,View
import os
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from student.models import Student,State,City,Country
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa






class SecurityView(LoginRequiredMixin,TemplateView):
    form_class = SecuritySignUpForm
    template_name = "admin_temp/security_list.html"
 
    def post(self, request):
        security_form = SecuritySignUpForm()
        if request.method == 'POST':
            security_form = SecuritySignUpForm(request.POST)
            if security_form.is_valid():
                security_form.save()
                username = security_form.cleaned_data.get('username')
                messages.success(request, f'Your Security has been created!!' + username)
            return redirect('securities:security_list')
        return render(request, "admin_temp/security_list.html")
       
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            securities = Security.objects.all()           
            security_form = SecuritySignUpForm()
            context = {'security_form':security_form, 'securities':securities   }
            return context
 


class SecurityProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'admin_temp/security_profile.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Security.objects.filter(user=self.request.user)

        account_delete_form = UserDeleteForm()
        deactivate_form = UserDeactivateForm()
        context = {'deactivate_form': deactivate_form,
                   'account_delete_form': account_delete_form, 'profile': profile, }
        return context

class UserDeactivateView(LoginRequiredMixin, View):
    """
    Deactivates the currently signed-in user by setting is_active to False.
    """

    def get(self, request, *args, **kwargs):
        deactivate_form = UserDeactivateForm()
        return render(request, 'admin_temp/security_profile.html', {'deactivate_form': deactivate_form})

    def post(self, request, *args, **kwargs):
        deactivate_form = UserDeactivateForm(request.POST)
        if deactivate_form.is_valid():
            request.user.is_active = False
            request.user.save()
            logout(request)
            messages.success(request, 'Account successfully deactivated')
            return redirect(reverse('home:admin_login'))
        return render(request, 'admin_temp/security_profile.html', {'deactivate_form': deactivate_form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """

    def get(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm()
        return render(request, 'admin_temp/security_profile.html', {'account_delete_form': account_delete_form})

    def post(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm(request.POST)
        if account_delete_form.is_valid():
            user = request.user
            logout(request)
            user.delete()
            messages.success(request, 'Account permanently deleted')
            return redirect(reverse('home:admin_login'))
        return render(request, 'admin_temp/security_profile.html', {'account_delete_form': account_delete_form})


def security_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    security = get_object_or_404(Security, pk=pk)
    template_path = 'admin_temp/security_printer.html'
    context = {'security': security}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="security_report.pdf"'
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
    return render(request, 'admin_temp/city_dropdown_list_options.html', {'state': state})


def load_cities(request):   
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()   
    return render(request, 'admin_temp/city_dropdown_list_options.html', {'cities':cities})


class SecurityUpdateProfile(LoginRequiredMixin,TemplateView):
    from_class = SecurityProfileForm
    template_name = 'admin_temp/security_profile_update.html'
    success_url = reverse_lazy('securities:profile_update')

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        security_profile_form = Security.objects.get_or_create(user=self.request.user)
        security_profile_form = SecurityProfileForm(post_data, file_data, instance=request.user.security)
        if security_profile_form.is_valid():           
            security_profile_form.save()
            messages.success(request, 'Your profile Update  succesfully!')
            return redirect('securities:profile_update')

        context = self.get_context_data(
            security_profile_form=security_profile_form

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
    template_name = 'admin_temp/security_profile.html'
    success_url = reverse_lazy('securities:security_profile')

    def form_valid(self,form):
        messages.success(self.request, 'Your Password changed  succesfully!')
        return super().form_valid(form)








 

   
   
        


   
