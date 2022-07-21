
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from superadmin.models import Notification
from .forms import TestNotification
from firebase_admin.messaging import Message
from fcm_django.models import FCMDevice

from django.views.generic import TemplateView, CreateView
from django.contrib.auth import get_user_model
User = get_user_model()



@login_required
def index_page(request):
    notify_form = TestNotification()
    if request.method == "POST":
        notify_form = TestNotification(request.POST)
        if notify_form.is_valid():                  
            # notify_form.save()           
            message_obj = Message(
                data={
                    'title': notify_form.cleaned_data.get('title'),
                    'body': notify_form.cleaned_data.get('body'),
                    'icon_url': notify_form.cleaned_data.get('icon_url'),
                    'url': notify_form.cleaned_data.get('url'),
                },
            )
            devices = FCMDevice.objects.filter(user_id=notify_form.cleaned_data.get('user_id'))
            if devices.exists():
                print(devices)
            # devices = FCMDevice.objects.all().first()
       
            # devices.send_message(message_obj)
            return redirect('notifications:user_notify')
        messages.error(
            request, "Unsuccessful. Invalid information.")
    notify_form = TestNotification()
    push_message = Notification.objects.all()
    return render(request, 'admin_temp/notify_index.html', {"notify_form": notify_form,"push_message":push_message})








# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm

# from .forms import NewUserForm


# def register_page(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("login")
#         messages.error(
#             request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render(request=request, template_name="accounts/register.html", context={"register_form": form})


# def login_page(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("index")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="accounts/login.html", context={"login_form": form})

# def logout_request(request):
# 	logout(request)
# 	messages.info(request, "You have successfully logged out.") 
# 	return redirect("index")
