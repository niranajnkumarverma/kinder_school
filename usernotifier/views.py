from django.shortcuts import render

# Create your views here.

  
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "admin_temp/user_notifier.html"