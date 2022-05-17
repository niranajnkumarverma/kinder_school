from django.urls import path
from admin_portal.admin.views import AddImageView, AddVideoView, AdminLogoutView, AdminUser, ImageDeleteView, ImageUpdateView, VideoDeleteView, VideoListView, VideoUpdateView, adminlogin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    path('home/', AdminUser.as_view() , name='home'),
    # path('admin_login/', AdminLogin.as_view() , name='admin_login'),
    path('admin_login',adminlogin, name='admin_login'),
    path('admin_logout',AdminLogoutView.as_view(), name='admin_logout'),
    
  ##....................Video url .................##

    path('video_list/', VideoListView.as_view() , name='video_list'),
    path('video_add/', AddVideoView.as_view() , name='video_add'),
    path('video_update/<int:pk>/', VideoUpdateView.as_view() , name= 'video_update'),
    path('video_delete/<int:pk>/', VideoDeleteView.as_view() , name= 'video_delete'),

    ##....................Image url .................##

    # path('image/', ImageListView.as_view() , name='image_list'),
    path('image_add/', AddImageView.as_view() , name='image_add'),
    path('image_update/<int:pk>/', ImageUpdateView.as_view() , name= 'image_update'),
    path('image_delete/<int:pk>/', ImageDeleteView.as_view() , name= 'image_delete'),
  



    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
