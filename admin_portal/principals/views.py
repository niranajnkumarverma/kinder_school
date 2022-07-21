from admin_portal.principals.forms import PrincipalProfile, PrincipalSignUpForm, UserDeactivateForm, UserDeleteForm
from principal.models import Principal
from django.urls import reverse_lazy
from home.models import User
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



# class Add_TeacherView(CreateView):
#     form_class = TeacherProfile
#     template_name = "admin_temp/add-teacher.html"
#     success_url = reverse_lazy('teachers:add_teachers')


class PrincipalView(LoginRequiredMixin, TemplateView):
    form_class = PrincipalSignUpForm
    template_name = "admin_temp/principals_list.html"

    def post(self, request):
        principal_form = PrincipalSignUpForm()
        if request.method == 'POST':
            principal_form = PrincipalSignUpForm(request.POST)
            if principal_form.is_valid():
                principal_form.save()
                username = principal_form.cleaned_data.get('username')
                messages.success(
                    request, f'Your Principal has been created!!' + username)
            return redirect('principals:principals_list')
        return render(request, "admin_temp/principals_list.html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        principals = Principal.objects.all()
        principal_form = PrincipalSignUpForm()
        context = {'principal_form': principal_form, 'principals': principals}
        return context


class PrincipalProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_temp/principal_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Principal.objects.filter(user=self.request.user)

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
        return render(request, 'admin_temp/principal_profile.html', {'account_delete_form': account_delete_form})

    def post(self, request, *args, **kwargs):
        account_delete_form = UserDeleteForm(request.POST)
        if account_delete_form.is_valid():
            user = request.user
            logout(request)
            user.delete()
            messages.success(request, 'Account permanently deleted')
            return redirect(reverse('home:admin_login'))
        return render(request, 'admin_temp/principal_profile.html', {'account_delete_form': account_delete_form})



def principal_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    principal = get_object_or_404(Principal, pk=pk)
    template_path = 'admin_temp/principal_printer.html'
    context = {'principal': principal}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="principal_report.pdf"'
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
    return render(request, 'admin_temp/city_dropdown_list_options.html', {'cities': cities})


class PrincipalUpdateProfile(LoginRequiredMixin, TemplateView):
    from_class = PrincipalProfile
    template_name = 'admin_temp/principal_profile_update.html'
    success_url = reverse_lazy('principals:profile_update')

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        principal_profile_form = Principal.objects.get_or_create(
            user=self.request.user)
        principal_profile_form = PrincipalProfile(
            post_data, file_data, instance=request.user.principal)

        if principal_profile_form.is_valid():

            principal_profile_form.save()
            messages.success(request, 'Your profile Update  succesfully!')
            return redirect('principals:profile_update')

        context = self.get_context_data(
            principal_profile_form=principal_profile_form

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
    template_name = 'admin_temp/principal_profile.html'
    success_url = reverse_lazy('principals:principal_profile')

    def form_valid(self, form):
        messages.success(self.request, 'Your Password changed  succesfully!')
        return super().form_valid(form)
