from django.urls import path
from student.views import  ProfileView, UserLogin, StudentUpdateProfile, ChangePasswordView


app_name = 'student'

urlpatterns = [
      path('login/', UserLogin.as_view(), name='login'),
      path('student_profile/',ProfileView.as_view(), name='student_profile'),
      path('profile_update/',StudentUpdateProfile.as_view(), name='profile_update'),
      path('password-change/', ChangePasswordView.as_view(), name='password_change'),
     
    
]