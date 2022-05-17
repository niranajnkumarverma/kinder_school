from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from home.models import Student, Teacher
from admin_portal.teachers.forms import TeacherProfile, TeacherSignUpForm
from django.urls import reverse_lazy
from home.models import User
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# class Add_TeacherView(CreateView):
#     form_class = TeacherProfile
#     template_name = "admin_temp/add-teacher.html"
#     success_url = reverse_lazy('teachers:add_teachers')

def create_teacher(request):
    teachers = Teacher.objects.all()
    teacher_form = TeacherSignUpForm()
    if request.method == 'POST':
        teacher_form = TeacherSignUpForm(request.POST)
        if teacher_form.is_valid():
                teacher_form.save()
                username = teacher_form.cleaned_data.get('username')
                messages.success(request, f'Your Teacher has been created!!'+ username)
                return redirect('teachers:add_teachers')  
    return render(request, 'admin_temp/add-teacher.html', {"teacher_form": teacher_form,"teachers":teachers})


# class Delete_teacher(LoginRequiredMixin,View):
#     def get(self, request, pk):
#         user = User.objects.get(pk=self.kwargs['pk'])
#         print("<<<<<<<<<<<<<",user)
#         if user.is_teacher:
#             user.delete()
#             # messages.success(self.request, f'Teacher has been deleted!')
#         return redirect('/')


def delete_teacher(request,username):
    try:
        u = User.objects.get(username = username)
        u.delete()
        # messages.sucess(request, "The user is deleted")
    except:
      messages.error(request, "The user not found")    
    return render(request, 'admin_temp/add-teacher.html')  