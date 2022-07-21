import django
from django.conf import settings
from django.urls import path
from student.forms import UserPasswordResetForm
from student.views import  ProfileView, StudentProfile, ChangePasswordView, UserDeactivateView, UserDeleteView, load_cities, load_state, student_render_pdf_view
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'student'

urlpatterns = [
    path('ajax/load-state/', load_state, name='ajax_load_state'), # AJAX
    path('ajax/load-cities/',load_cities, name='ajax_load_cities'), # AJAX


   
    path('student-pdf/<pk>/',student_render_pdf_view, name='student-pdf-view'), 

    path('student_profile/', ProfileView.as_view(), name='student_profile'),
    path('user_account/', UserDeactivateView.as_view(), name='user_account'),
    path('user_delete/', UserDeleteView.as_view(), name='user_delete'),
  

    path('profile_update/', StudentProfile.as_view(), name='profile_update'),
    # path('profile_update/',StudentUpdateProfile.as_view(), name='profile_update'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    path("password-reset/",
         PasswordResetView.as_view(
             template_name='user/password_reset.html', form_class=UserPasswordResetForm),
         name="password_reset",),

   	path("",
         PasswordResetDoneView.as_view(
             template_name='user/index.html'
         ),
         name="password_reset_done"),

   	path("password-reset-confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html'),
         name="password_reset_confirm"),

   	path("password-reset-complete/",
         PasswordResetCompleteView.as_view(
             template_name='user/password_reset_complete.html'),
         name="password_reset_complete"),

      
     
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)