from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from chatbot.views import mainpage



app_name = 'chatbot'
urlpatterns = [   
    path('', mainpage.as_view(), name='chat_index'),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)