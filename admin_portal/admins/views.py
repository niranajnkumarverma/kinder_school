
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from principal.models import Principal
from superadmin.models import  Address, AdminProfileModel, FooterBackground, HeaderBackground, Image, Logo, Title, Video
from admin_portal.admins.forms import Addressform, AdminLoginForm, AdminProfile, CityCsvImportForm,CountryCsvImportForm, ImageForm, Logoform, StateCsvImportForm, Titleform, UpdateImageForm, UserDeactivateForm, UserDeleteForm, VideoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.views import LoginView 
from django.contrib.auth import login 
from django.contrib.auth import REDIRECT_FIELD_NAME, logout as auth_logout
from django.views.generic import RedirectView
from django.contrib import messages
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
import os
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from student.models import State, City, Country
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

#######...........Admin Login .........############

from django.shortcuts import render
from django.urls import path
from django import forms
from student.models import Code, Student, User,State,City,Country
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse




class AdminUser(TemplateView):
    template_name = "admin_temp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_title = Title.objects.all().first()       
        context = {'site_title': site_title }
        return context





class AdminProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_temp/admin_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = AdminProfileModel.objects.filter(user=self.request.user)
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
        return render(request, 'admin_temp/principal_profile.html', {'deactivate_form': deactivate_form})

    def post(self, request, *args, **kwargs):
        deactivate_form = UserDeactivateForm(request.POST)
        if deactivate_form.is_valid():
            request.user.is_active = False
            request.user.save()
            logout(request)
            messages.success(request, 'Account successfully deactivated')
            return redirect(reverse('home:admin_login'))
        return render(request, 'admin_temp/principal_profile.html', {'deactivate_form': deactivate_form})


class UserDeleteView(LoginRequiredMixin, View):
    """
    Deletes the currently signed-in user and all associated data.
    """

    def get(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm()
        return render(request, 'admin_temp/admin_profile.html', {'account_delete_form': account_delete_form})

    def post(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm(request.POST)
        if account_delete_form.is_valid():
            user = request.user
            logout(request)
            user.delete()
            messages.success(request, 'Account permanently deleted')
            return redirect(reverse('home:admin_login'))
        return render(request, 'admin_temp/admin_profile.html', {'account_delete_form': account_delete_form})





# AJAX
def load_state(request):
    country_id = request.GET.get('country_id')
    state = State.objects.filter(country_id=country_id).all()
    return render(request, 'admin_temp/city_dropdown_list_options.html', {'state': state})


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).all()
    return render(request, 'admin_temp/city_dropdown_list_options.html', {'cities': cities})


class AdminUpdateProfile(LoginRequiredMixin, TemplateView):
    from_class = AdminProfile
    template_name = 'admin_temp/admin_profile_update.html'
    success_url = reverse_lazy('home:profile_update')

    def post(self, request):

        admin_profile_form = AdminProfile(request.POST)
        # admin_profile_form = Admin.objects.get_or_create(user=request.user)
        if admin_profile_form.is_valid():

            admin_profile_form.save()
            messages.success(request, 'Your profile Update  succesfully!')
            return redirect('home:admin_update')

        context = self.get_context_data(
            admin_profile_form=admin_profile_form

        )
        return self.render_to_response(context)

    def get(self, request,  *args, **kwargs):
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
    template_name = 'admin_temp/admin_profile.html'
    success_url = reverse_lazy('home:admin_profile')

    def form_valid(self, form):
        messages.success(self.request, 'Your Password changed  succesfully!')
        return super().form_valid(form)




def adminlogin(request):
    admin_login_form = AdminLoginForm(request.POST or None)
    if request.POST and admin_login_form.is_valid():
        user = admin_login_form.login(request)
        if user.is_superuser:
            login(request, user)
            messages.success(request,"You are Login Succesfully!!")
            return redirect("home:home")   
        else:
            if user.is_principal:
                login(request, user)
                messages.success(request,"You are Login Succesfully!!")
                return redirect("home:home")   
            else:
                if user.is_teacher:
                        login(request, user)
                        messages.success(request,"You are Login Succesfully!!")
                        return redirect("home:home")  
                else:
                    if user.is_security:
                        login(request,user)
                        messages.success(request,"You are Login Succesfully!!")
                        return redirect("home:home")  
                    else:
                        if user.is_parent:
                            login(request,user)
                            messages.success(request,"You are Login Succesfully!!")
                            return redirect("home:home")                  
    return render(request, 'admin_temp/login.html',{'admin_login_form': admin_login_form })



class Backgroundlist(LoginRequiredMixin,TemplateView):
    template_name = "admin_temp/background_list.html"
    success_url = reverse_lazy('home:change_color')
     
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            footer = FooterBackground.objects.all()
            header = HeaderBackground.objects.all() 
         
            context = {'footer': footer, 'header':header }
            return context


def header(request):   
    if request.method == 'POST': 
        color = request.POST['color']
        background=HeaderBackground.objects.create(
            color=color
        )
        background.save()
        messages.success(request, 'Header Background color post successfully!')
    footer = FooterBackground.objects.all()    
    header = HeaderBackground.objects.all()    
    return render(request, "admin_temp/background_list.html", {'header': header, 'footer': footer, })


def header_update(request,pk):
    if request.method == 'POST': 
        header = HeaderBackground.objects.get(pk=pk)   
        header.color = request.POST['color']
        header.save()
        messages.success(request, f'Header color update Successfully!')
        return redirect('home:change_color')         
    return render(request, "admin_temp/header_color_update.html")  


class HeaderDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        user = request.user
        header = HeaderBackground.objects.get(pk=self.kwargs['pk'])
        if header:
            header.delete()
            messages.success(self.request, f'Header has been deleted Successfully!')
        return redirect('home:change_color')    




def footer(request):   
    if request.method == 'POST': 
        color = request.POST['color']
        background=FooterBackground.objects.create(
            color=color
        )
        background.save()
        messages.success(request, 'Footer Background color post successfully!')
     
    footer = FooterBackground.objects.all()
    header = HeaderBackground.objects.all()    
    return render(request, "admin_temp/background_list.html", {'header': header,'footer': footer,  })


def footer_update(request,pk):
    if request.method == 'POST': 
        footer = FooterBackground.objects.get(pk=pk)   
        footer.color = request.POST['color']
        footer.save()
        messages.success(request, f'Footer color update Successfully!')
        return redirect('home:change_color') 
    return render(request, "admin_temp/footer_color_update.html")

class FooterDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        user = request.user
        footer = FooterBackground.objects.get(pk=self.kwargs['pk'])
        if footer:
            footer.delete()
            messages.success(self.request, f'Footer has been deleted Successfully!')
        return redirect('home:change_color')   

  

class AddressView(LoginRequiredMixin,CreateView):
    model = Address
    from_class = Addressform
    fields= '__all__'
    template_name = "admin_temp/cms.html"
    success_url = reverse_lazy('home:cms_view')

    def form_valid(self, form):
        messages.success(self.request, f"Your Address has been Added succesfully")
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            site_logos = Logo.objects.all()
            site_title = Title.objects.all()
            site_address = Address.objects.all()
            title_form = Titleform()
            address_form = Addressform()
            logo_form = Logoform()
        
            context = {'logo_form': logo_form, 'site_logos': site_logos,'title_form':title_form,'site_title':site_title,'address_form':address_form,'site_address':site_address }
            return context

class AddressUpdateView(LoginRequiredMixin,UpdateView):
    model = Address   
    fields=  '__all__'
    template_name = "admin_temp/address_update.html"
    success_url = reverse_lazy('home:cms_view')
    
    def form_valid(self, form):
        messages.success(
            self.request, f"Your Address has been Updated succesfully")
        return super().form_valid(form)


class AddressDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        user = request.user
        address = Address.objects.get(pk=self.kwargs['pk'])
        if address:
            address.delete()
            messages.success(self.request, f'Address has been deleted Successfully!')
        return redirect('home:cms_view')



class TitleView(LoginRequiredMixin,CreateView):
    model = Title
    from_class = Titleform
    fields= ['site_title']
    template_name = "admin_temp/cms.html"
    success_url = reverse_lazy('home:cms_view')

    def form_valid(self, form):
        messages.success(self.request, f"Your Title has been Added succesfully")
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            site_logos = Logo.objects.all()
            site_title = Title.objects.all()
            site_address = Address.objects.all()
            title_form = Titleform()
            address_form = Addressform()
            logo_form = Logoform()
        
            context = {'logo_form': logo_form, 'site_logos': site_logos,'title_form':title_form,'site_title':site_title,'address_form':address_form,'site_address':site_address }
            return context


class TitleUpdateView(LoginRequiredMixin,UpdateView):
    model = Title   
    fields= ['site_title']
    template_name = "admin_temp/title_update.html"
    success_url = reverse_lazy('home:cms_view')
    
    def form_valid(self, form):
        messages.success(
            self.request, f"Your Title has been Updated succesfully")
        return super().form_valid(form)


class TitleDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        user = request.user
        title = Title.objects.get(pk=self.kwargs['pk'])
        if title:
            title.delete()
            messages.success(self.request, f'Title has been deleted Successfully!')
        return redirect('home:cms_view')


class CMsView(LoginRequiredMixin,CreateView):
    model = Logo
    from_class = Logoform
    fields= ['site_logo']
    template_name = "admin_temp/cms.html"
    success_url = reverse_lazy('home:cms_view')

    def form_valid(self, form):
        messages.success(self.request, f"Your Logo has been Updated succesfully")
        return super().form_valid(form)
       

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_logos = Logo.objects.all()
        site_title = Title.objects.all()
        site_address = Address.objects.all()
        title_form = Titleform()
        address_form = Addressform()
        logo_form = Logoform()
       
        context = {'logo_form': logo_form, 'site_logos': site_logos,'title_form':title_form,'site_title':site_title,'address_form':address_form,'site_address':site_address }
        return context

class LogoUpdateView(LoginRequiredMixin,UpdateView):
    model = Logo   
    fields= ['site_logo']
    template_name = "admin_temp/logo_update.html"
    success_url = reverse_lazy('home:cms_view')
    
    def form_valid(self, form):
        messages.success(
            self.request, f"Your Logo has been Updated succesfully")
        return super().form_valid(form)


class LogoDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        user = request.user
        logo = Logo.objects.get(pk=self.kwargs['pk'])
        if logo:
            logo.delete()
            messages.success(self.request, f'logo has been deleted Successfully!')
        return redirect('home:cms_view')
   

def country_upload_csv(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_upload"]
        
        if not csv_file.name.endswith('.csv'):
            messages.warning(request, 'The wrong file type was uploaded')
            return HttpResponseRedirect(request.path_info)
        
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")

        for x in csv_data:
            fields = x.split(",")
            created = Country.objects.update_or_create(
                name = fields[0],
                # balance = fields[1],
                )
            
        url = reverse('home:state_upload_csv')
        messages.success(request, 'The Country Csv File Uploaded Successfully')
        return HttpResponseRedirect(url)

    country_form = CountryCsvImportForm()
    countries = Country.objects.all()
    
    return render(request, "admin_temp/csv_upload.html", {'country_form':country_form,'countries':countries})



def state_upload_csv(request):  
    if request.method == "POST":
        csv_file = request.FILES["csv_upload"]        
        if not csv_file.name.endswith('.csv'):
            messages.warning(request, 'The wrong file type was uploaded')
            return HttpResponseRedirect(request.path_info)
        
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")

        for x in csv_data:
            fields = x.split(",")
    
            created = State.objects.update_or_create(country_id=77,
                name = fields[0],
                # country_id=fields[2],
                # balance = fields[1],
                )
            
        url = reverse('home:city_upload_csv')
        messages.success(request, f'The State Csv File Uploaded Successfully')
        return HttpResponseRedirect(url)

    state_form = StateCsvImportForm()
    states = State.objects.all()    
    return render(request, "admin_temp/csv_upload.html", {'state_form':state_form, 'states':states})



def city_upload_csv(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_upload"]        
        if not csv_file.name.endswith('.csv'):
            messages.warning(request, 'The wrong file type was uploaded')
            return HttpResponseRedirect(request.path_info)
        
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\n")

        for x in csv_data:
            fields = x.split(",")
            created = City.objects.update_or_create(state_id=11,
                name = fields[0],
                # balance = fields[1],
                )
        url = reverse('home:city_upload_csv')
        messages.success(request, f'The City Csv File Uploaded Successfully')
        return HttpResponseRedirect(url)

    city_form = CityCsvImportForm()
    cities = City.objects.all()
    return render(request, "admin_temp/csv_upload.html", {'cities':cities, 'city_form':city_form})


 
#######..............Video part ................#####

# class VideoListView(ListView):
#     model = Video
#     template_name = "admin_temp/video_list.html"


class AddVideoView(LoginRequiredMixin,CreateView):
    from_class = VideoForm
    fields = ["name", "videofile", ]
    queryset = Video.objects.all()
    success_url = reverse_lazy('home:video_add')
    template_name = "admin_temp/video_list.html"

    def form_valid(self, form):
        messages.success(
            self.request, f"Your Video has been Added succesfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            videos = Video.objects.all()
            context['videos'] = videos
            return context

class VideoUpdateView(LoginRequiredMixin,UpdateView):
    model = Video
    fields = ["name", "videofile", ]
    template_name = "admin_temp/video_update.html"
    success_url = reverse_lazy('home:video_add')

    def form_valid(self, form):
        messages.success(
            self.request, f"Your Video has been Updated succesfully")
        return super().form_valid(form)


class VideoDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        user = request.user
        video = Video.objects.get(pk=self.kwargs['pk'])
        if video:
            video.delete()
            messages.success(
                self.request, f'Video has been deleted Successfully!')
        return redirect('home:video_add')


## ....................Image part ....................###

# class ImageListView(ListView):
#     model = Image
#     template_name = "admin_temp/image_lis.html"


class AddImageView(LoginRequiredMixin,CreateView):
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


class ImageUpdateView(LoginRequiredMixin,UpdateView):
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


class ImageDeleteView(LoginRequiredMixin,View):
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