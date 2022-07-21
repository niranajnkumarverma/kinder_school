from email import message
from django.urls import path
from .views import AboutView, CourseView, EventView, GalleryView, LogoutView, TeacherView,contact, index, login_view, otp_page, resend_otp,  signup, verify_otp, verify_view


# app_name = 'home'

urlpatterns = [
    #   path('', IndexView.as_view(), name='index'),
    #   path('signup/', SignUpView.as_view(), name='signup'),
    #   path('login/', UserLogin.as_view(), name='login'),

    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),

  
    #  Email SEND OTP, OTP PAGE, VERIFIY OTP AND FUNCTIOALITY
    path('otp_page/', otp_page, name='otp_page'),
    #path('verify_otp/', verify_otp, name='verify_otp'),
    path('verify_otp/<str:verify_for>/', verify_otp, name='otp_verify'),
    ## Twillio Mobile OTP verification
    path('verify/', verify_view, name='verify-view'),
    path('resendOTP/', resend_otp, name='resendOTP'),

    path('contactview/', contact, name='contactview'),


   
    # path('contactview/', ContactView.as_view(), name='contactview'),
    
    
    path('teacherview/', TeacherView.as_view(), name='teacherview'),
    path('aboutview/', AboutView.as_view(), name='aboutview'),
    path('courseview/', CourseView.as_view(), name='courseview'),
    path('galleryview/', GalleryView.as_view(), name='galleryview'),
    path('eventview/', EventView.as_view(), name='eventview'),
    path('logout/', LogoutView.as_view(), name='logout'),



]
