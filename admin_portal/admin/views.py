from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from admin_portal.admin.forms import AdminLoginForm, ImageForm, UpdateImageForm, VideoForm
from home.models import Video, Image
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.views import LoginView 
from django.contrib.auth import login 
from django.contrib.auth import REDIRECT_FIELD_NAME, logout as auth_logout
from django.views.generic import RedirectView

#######...........Admin Login .........############

class AdminUser(TemplateView):
    template_name = "admin_temp/index.html"


# class AdminLogin(LoginView):
#     template_name = "admin_temp/login.html"

def adminlogin(request):
    admin_login_form = AdminLoginForm(request.POST or None)
    if request.POST and admin_login_form.is_valid():
        user = admin_login_form.login(request)
        if user.is_admin:
            login(request, user)
            return redirect("home:home")   
        else:
            if user.is_principal:
                login(request, user)
                return redirect("home:home")   
            else:
                if user.is_teacher:
                        login(request, user)
                        return redirect("home:home")  
                else:
                    if user.is_staff:
                        login(request,user)
                        messages.success(request,"You are Login Succesfully!!")
                        return redirect("home:home")   
    return render(request, 'admin_temp/login.html',{'admin_login_form': admin_login_form })
 
#######..............Video part ................#####

class VideoListView(ListView):
    model = Video
    template_name = "admin_temp/video_list.html"


class AddVideoView(CreateView):
    from_class = VideoForm
    fields = ["name", "videofile", ]
    queryset = Video.objects.all()
    success_url = reverse_lazy('home:video_add')
    template_name = "admin_temp/video_add.html"

    def form_valid(self, form):
        messages.success(
            self.request, f"Your Video has been Added succesfully")
        return super().form_valid(form)


class VideoUpdateView(UpdateView):
    model = Video
    fields = ["name", "videofile", ]
    template_name = "admin_temp/video_update.html"
    success_url = reverse_lazy('home:video_list')

    def form_valid(self, form):
        messages.success(
            self.request, f"Your Video has been Updated succesfully")
        return super().form_valid(form)


class VideoDeleteView(View):
    def get(self, request, pk):
        user = request.user
        video = Video.objects.get(pk=self.kwargs['pk'])
        if video:
            video.delete()
            messages.success(
                self.request, f'Video has been deleted Successfully!')
        return redirect('home:video_list')


## ....................Image part ....................###

# class ImageListView(ListView):
#     model = Image
#     template_name = "admin_temp/image_lis.html"


class AddImageView(CreateView):
    model = Image
    from_class = ImageForm
    fields = ["name", "school_image", ]
    success_url = reverse_lazy('home:image_add')
    template_name = "admin_temp/image_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = Image.objects.all()
        context['images'] = images
        return context
 
    

    def form_valid(self, form):
        messages.success(
            self.request, f"Your Event Image has been Added Succesfully")
        return super().form_valid(form)


class ImageUpdateView(UpdateView):
    model = Image
    from_class = UpdateImageForm
    fields = ["name", "school_image", ]
    template_name = "admin_temp/image_list.html"
    success_url = reverse_lazy('home:image_add')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)   
        image_form = UpdateImageForm()
        context['image_form']= image_form
        return context

    def form_valid(self, form):
        messages.success(
            self.request, f"Your Event image has been Update Succesfully")
        return super().form_valid(form)


class ImageDeleteView(View):
    def get(self, request, pk):
        user = request.user
        image = Image.objects.get(pk=self.kwargs['pk'])
        if image:
            image.delete()
            messages.success(
                request, 'Event Image has been deleted Successfully!')
        return redirect('home:image_add')



class AdminLogoutView(RedirectView):
    url = 'admin_login'
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(AdminLogoutView, self).get(request, *args, **kwargs)