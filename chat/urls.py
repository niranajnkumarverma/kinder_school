from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from chat.views import index, room_view





app_name = 'chat'
urlpatterns = [   
    path('',index, name='chat'),
    path('<str:room_name>/', room_view, name='chat-room'),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)