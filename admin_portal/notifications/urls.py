from django.urls import path

from .views import index_page





app_name = 'notifications'

urlpatterns = [
   
    path('user_notify/',index_page, name='user_notify'),

]
  
