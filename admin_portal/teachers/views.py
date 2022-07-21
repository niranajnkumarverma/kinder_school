from teacher.models import Teacher
from admin_portal.teachers.forms import TeacherProfile, TeacherSignUpForm, UserDeactivateForm, UserDeleteForm
from django.urls import reverse_lazy
from home.models import User
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
from django.urls import reverse
from django.contrib.auth import logout
from django.template.loader import get_template
from xhtml2pdf import pisa



class TeachersView(LoginRequiredMixin,TemplateView):
    form_class = TeacherSignUpForm
    template_name = "admin_temp/teacher_list.html"
 
    def post(self, request):
        teacher_form = TeacherSignUpForm()
        if request.method == 'POST':
            teacher_form = TeacherSignUpForm(request.POST)
            if teacher_form.is_valid():
                teacher_form.save()
                username = teacher_form.cleaned_data.get('username')
                messages.success(request, f'Your Teacher has been created!!' + username)
            return redirect('teachers:teachers_list')
        return render(request, "admin_temp/teacher_list.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teachers = Teacher.objects.all()
        teacher_form = TeacherSignUpForm()
        context = {'teacher_form': teacher_form, 'teachers': teachers}
        return context



class TeacherProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'admin_temp/teacher_profile.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Teacher.objects.filter(user=self.request.user)
        account_delete_form = UserDeleteForm()
        deactivate_form = UserDeactivateForm()
        context = {'deactivate_form':deactivate_form, 'account_delete_form':account_delete_form    ,'profile':profile,}
        return context

class UserDeactivateView(LoginRequiredMixin, View):
    """
    Deactivates the currently signed-in user by setting is_active to False.
    """

    def get(self, request, *args, **kwargs):
        deactivate_form = UserDeactivateForm()
        return render(request, 'admin_temp/teacher_profile.html', {'deactivate_form': deactivate_form})

    def post(self, request, *args, **kwargs):
        deactivate_form = UserDeactivateForm(request.POST)
        if deactivate_form.is_valid():
            request.user.is_active = False
            request.user.save()
            logout(request)
            messages.success(request, 'Account successfully deactivated')
            return redirect(reverse('home:admin_login'))
        return render(request, 'admin_temp/teacher_profile.html', {'deactivate_form': deactivate_form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """

    def get(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm()
        return render(request, 'admin_temp/user_deletion.html', {'account_delete_form': account_delete_form})

    def post(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm(request.POST)
        if account_delete_form.is_valid():
            user = request.user
            logout(request)
            user.delete()
            messages.success(request, 'Account successfully deleted')
            return redirect(reverse('home:admin_login'))
        return render(request, 'admin_temp/teacher_profile.html', {'account_delete_form': account_delete_form})


def teacher_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    teacher = get_object_or_404(Teacher, pk=pk)
    template_path = 'admin_temp/teacher_printer.html'
    context = {'teacher': teacher}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="teacher_report.pdf"'
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


class TeacherupdateProfile(LoginRequiredMixin,TemplateView):
    from_class = TeacherProfile
    template_name = 'admin_temp/teacher_profile_update.html'
    success_url = reverse_lazy('teachers:profile_update')

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        teacher_profile_form = Teacher.objects.get_or_create(user=self.request.user)
        teacher_profile_form = TeacherProfile(post_data, file_data, instance=request.user.teacher)       
        if teacher_profile_form.is_valid():
            teacher_profile_form.save()
            messages.success(request, 'Your profile Update  succesfully!')
            return redirect('teachers:profile_update')

        context = self.get_context_data(
            teacher_profile_form=teacher_profile_form

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
    template_name = 'admin_temp/teacher_profile.html'
    success_url = reverse_lazy('teachers:teacher_profile')

    def form_valid(self,form):
        messages.success(self.request, 'Your Password changed  succesfully!')
        return super().form_valid(form)













class Delete_teacher(LoginRequiredMixin,DeleteView):
    def get(self, request, pk):
        user = request.user
        user = User.objects.get(pk=self.kwargs['pk'])
        if user.is_teacher:
            user.delete()
            messages.success(
                request, 'Your User has been Deleted succesfully!')
        
        return redirect('teachers:teachers_list')




