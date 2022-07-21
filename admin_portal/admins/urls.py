from django.urls import path
from student.forms import UserPasswordResetForm
from admin_portal.admins.views import AddImageView, AddVideoView, AddressDeleteView, AddressUpdateView, AddressView, AdminLogoutView, AdminProfileView, AdminUpdateProfile, AdminUser, Backgroundlist, CMsView, ChangePasswordView, FooterDeleteView, HeaderDeleteView, ImageDeleteView, ImageUpdateView, LogoDeleteView, LogoUpdateView, TitleDeleteView, TitleUpdateView, TitleView, UserDeactivateView, UserDeleteView, VideoDeleteView,  VideoUpdateView, adminlogin, city_upload_csv, country_upload_csv, footer, footer_update, header, header_update,  load_cities, load_state, state_upload_csv
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import  PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
app_name = 'home'

urlpatterns = [
    path('home/', AdminUser.as_view() , name='home'),
    # path('admin_login/', AdminLogin.as_view() , name='admin_login'),
    path('admin_login',adminlogin, name='admin_login'),
    path('admin_logout',AdminLogoutView.as_view(), name='admin_logout'),
    
  ##....................Video url .................##

    # path('video_list/', VideoListView.as_view() , name='video_list'),
    path('video_add/', AddVideoView.as_view() , name='video_add'),
    path('video_update/<int:pk>/', VideoUpdateView.as_view() , name= 'video_update'),
    path('video_delete/<int:pk>/', VideoDeleteView.as_view() , name= 'video_delete'),

    ##....................Image url .................##

    # path('image/', ImageListView.as_view() , name='image_list'),
    path('image_add/', AddImageView.as_view() , name='image_add'),
    path('image_update/<int:pk>/', ImageUpdateView.as_view() , name= 'image_update'),
    path('image_delete/<int:pk>/', ImageDeleteView.as_view() , name= 'image_delete'),


    path('cms_view/', CMsView.as_view(), name='cms_view'),
    path('logo_update/<int:pk>/',LogoUpdateView.as_view(), name='logo_update'),
    path('logo_delete/<int:pk>/',LogoDeleteView.as_view(), name='logo_delete'),

    path('title_view/', TitleView.as_view(), name='title_view'),
    path('title_update/<int:pk>/',TitleUpdateView.as_view(), name='title_update'),
    path('title_delete/<int:pk>/',TitleDeleteView.as_view(), name='title_delete'),


    path('address_view/', AddressView.as_view(), name='address_view'),
    path('address_update/<int:pk>/',AddressUpdateView.as_view(), name='address_update'),
    path('address_delete/<int:pk>/',AddressDeleteView.as_view(), name='address_delete'),
  
  
    path('country_upload_csv/', country_upload_csv, name='country_upload_csv'),
    path('state_upload_csv/', state_upload_csv, name='state_upload_csv'),
    path('city_upload_csv/', city_upload_csv, name='city_upload_csv'),

    
    path("home/password-reset/",
         PasswordResetView.as_view(
             template_name='admin_temp/password_reset.html', form_class=UserPasswordResetForm),
         name="password_reset",),

   	path("home/admin_login",
         PasswordResetDoneView.as_view(
             template_name='admin_temp/login.html'
         ),
         name="password_reset_done"),

   	path("home/password-reset-confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(
             template_name='admin_temp/password_reset_confirm.html'),
         name="password_reset_confirm"),

   	path("home/password-reset-complete/",
         PasswordResetCompleteView.as_view(
             template_name='admin_temp/password_reset_complete.html'),
         name="admin_login/password_reset_complete"),


    path('change_color/', Backgroundlist.as_view(), name='change_color'),
    path('headerview/', header, name='headerview'),
    path('header_color_update/<int:pk>/', header_update, name='header_color_update'),
  
    path('header_delete/<int:pk>/',HeaderDeleteView.as_view(), name='header_delete'),


    path('footerview/', footer, name='footerview'),
    path('footer_color_update/<int:pk>/',footer_update, name='footer_color_update'),
    path('footer_delete/<int:pk>/',FooterDeleteView.as_view(), name='footer_delete'),

    path('ajax/load-state/', load_state, name='ajax_load_state'), # AJAX
    path('ajax/load-cities/',load_cities, name='ajax_load_cities'), # AJAX  
    path('admin_profile/', AdminProfileView.as_view(), name='admin_profile'),
    path('user_account/', UserDeactivateView.as_view(), name='user_account'),
    path('user_delete/', UserDeleteView.as_view(), name='user_delete'),
    path('profile_update/', AdminUpdateProfile.as_view(), name='profile_update'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
   

  

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
