from urllib import request
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import View
from django import views
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from student.forms import LoginForm, ProfileForm
from django.contrib.auth.views import LoginView  
from home.models import User
from order.models import Cart
from student.models import Profile
from django.views.generic.base import View
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView


class UserLogin(LoginView):
    from_class = LoginForm
    success_url = reverse_lazy('student:student_profile')
    template_name = 'user/index.html' 

    def form_valid(self,form):
        messages.success(self.request,"You are Login succesfully")
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'user/student_prof.html' 
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prof = Profile.objects.filter(user=self.request.user)
        context['address']=prof
        return context
 
           
class StudentUpdateProfile(LoginRequiredMixin,TemplateView):
    from_class = ProfileForm
    template_name = 'user/profile_update.html'
    success_url = reverse_lazy('student_profile')

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        # user_form = MyUserCreationForm(post_data, instance=request.user)
        profile_form = Profile.objects.get_or_create(user=self.request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)
       
        if profile_form.is_valid():
           
            profile_form.save()
            messages.success(request, 'Your profile Update  succesfully!')
            return redirect('student:student_profile')

        context = self.get_context_data(
            profile_form=profile_form

        )   
        return self.render_to_response(context)

    def get(self, request,  *args , **kwargs):
        return self.post(request, *args, **kwargs)     


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/student_prof.html'
    success_url = reverse_lazy('student:student_profile')

    def form_valid(self,form):
        messages.success(self.request, 'Your Password changed  succesfully!')
        return super().form_valid(form)















# class ChangePassword(LoginRequiredMixin,TemplateView):

#     def get(self, request, *args, **kwargs):
#         form_class = MyPasswordChangeForm
#         form = self.form_class(self.request.user)
#         return render(request, 'password.html',{'form': form,})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             return render(request, 'password.html', {'form': form, 'password_changed': True})
#         else:
#             return render(request, 'password.html', {'form': form, 'password_changed': False})

  
