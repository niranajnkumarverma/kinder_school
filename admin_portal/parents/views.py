import os
from django.urls import reverse_lazy
from admin_portal.parents.forms import ParentProfile, ParentSignUpForm, UserDeactivateForm, UserDeleteForm
from home.models import User
from django import forms
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView,View
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from parent.models import Parent



class ParentView(LoginRequiredMixin,TemplateView):
    form_class = ParentSignUpForm
    template_name = "admin_temp/parents_list.html"
 
    def post(self, request):
        parent_form = ParentSignUpForm()
        if request.method == 'POST':
            parent_form = ParentSignUpForm(request.POST)
            if parent_form.is_valid():
                parent_form.save()
                username = parent_form.cleaned_data.get('username')
                messages.success(request, f'Your Parent has been created!!' + username)
            return redirect('parents:parents_list')
        return render(request, "admin_temp/parents_list.html")
       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parents = Parent.objects.all()
        parent_form = ParentSignUpForm()
        context = {'parent_form': parent_form, 'parents': parents}
        return context
  


class ParentProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'admin_temp/parent_profile.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Parent.objects.filter(user=self.request.user)
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
        return render(request, 'admin_temp/parent_profile.html', {'deactivate_form': deactivate_form})

    def post(self, request, *args, **kwargs):
        deactivate_form = UserDeactivateForm(request.POST)
        if deactivate_form.is_valid():
            request.user.is_active = False
            request.user.save()
            logout(request)
            messages.success(request, 'Account successfully deactivated')
            return redirect(reverse('home:admin_login'))
        return render(request, 'admin_temp/parent_profile.html', {'deactivate_form': deactivate_form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """

    def get(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm()
        return render(request, 'admin_temp/parent_profile.html', {'account_delete_form': account_delete_form})

    def post(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm(request.POST)
        if account_delete_form.is_valid():
            user = request.user
            logout(request)
            user.delete()
            messages.success(request, 'Account permanently deleted')
            return redirect(reverse('home:admin_login'))
        return render(request, 'admin_temp/parent_profile.html', {'account_delete_form': account_delete_form})


def parent_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    parent = get_object_or_404(Parent, pk=pk)
    template_path = 'admin_temp/parent_printer.html'
    context = {'parent': parent}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="parent_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class ParentUpdateProfile(LoginRequiredMixin,TemplateView):
    from_class = ParentProfile
    template_name = 'admin_temp/parent_profile_update.html'
    success_url = reverse_lazy('parents:profile_update')

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        parent_profile_form = Parent.objects.get_or_create(user=self.request.user)
        parent_profile_form = ParentProfile(post_data, file_data, instance=request.user.parent)

        if parent_profile_form.is_valid():
            parent_profile_form.save()
            messages.success(request, 'Your profile Update  succesfully!')
            return redirect('parents:profile_update')

        context = self.get_context_data(
            parent_profile_form=parent_profile_form

        )
        return self.render_to_response(context)

    def get(self, request,  *args , **kwargs):
        return self.post(request, *args, **kwargs)     


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="applicxation/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404

  

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'admin_temp/parent_profile.html'
    success_url = reverse_lazy('parents:parent_profile')

    def form_valid(self,form):
        messages.success(self.request, 'Your Password changed  succesfully!')
        return super().form_valid(form)












   
   
        


   
   
        


   
