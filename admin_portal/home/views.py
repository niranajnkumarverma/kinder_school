from django.views.generic import TemplateView
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from admin_portal.home.forms import ImageForm, VideoForm
from home.models import Video,Image
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View


class AdminUser(TemplateView):
    template_name = "admin_temp/index.html"

class AdminLogin(TemplateView):
    template_name = "admin_temp/login.html"  


## ...................Video part ................##      

class VideoListView(ListView):
    model = Video
    template_name = "admin_temp/video_list.html"

class AddVideoView(CreateView):
    from_class = VideoForm
    fields= ["name", "videofile",]
    queryset = Video.objects.all()
    success_url = reverse_lazy('home:video_add')
    template_name = "admin_temp/video_add.html"

   
    def form_valid(self, form):
        messages.success(self.request,f"Your Video Added  succesfully")
        return super().form_valid(form)   
  
class VideoUpdateView(UpdateView):
    model = Video
    fields= ["name", "videofile",]
    template_name = "admin_temp/video_update.html"
    success_url = reverse_lazy('home:video_list')


    def form_valid(self, form):
        messages.success(self.request,f"Your Video Update  succesfully")
        return super().form_valid(form)

class VideoDeleteView(LoginRequiredMixin,View):
    def get(self, request,pk):
        user = request.user
        video = Video.objects.get(pk=self.kwargs['pk'])
        if video:
            video.delete()        
            messages.success(request, 'Video has been delete!')
        return redirect('home:video_list')  





## ....................Image part ....................###

class ImageListView(ListView):
    model = Image
    template_name = "admin_temp/image_list.html"

class AddImageView(CreateView):
    from_class = ImageForm
    fields= ["name", "schoolimage",]
    queryset = Image.objects.all()
    success_url = reverse_lazy('home:image_list')
    template_name = "admin_temp/image_add.html"

   
    def form_valid(self, form):
        messages.success(self.request,f"Your Event Image Added  succesfully")
        return super().form_valid(form)   
  
class ImageUpdateView(UpdateView):
    model = Image
    fields= ["name", "schoolimage",]
    template_name = "admin_temp/image_update.html"
    success_url = reverse_lazy('home:image_list')


    def form_valid(self, form):
        messages.success(self.request,f"Your Event image Update  succesfully")
        return super().form_valid(form)

class ImageDeleteView(LoginRequiredMixin,View):
    def get(self, request,pk):
        user = request.user
        video = Image.objects.get(pk=self.kwargs['pk'])
        if video:
            video.delete()        
            messages.success(request, 'Event Image has been delete!')
        return redirect('home:image_list')  





        
