from unicodedata import name
from django.urls import path
from admin_portal.students.views import StudentsView, UserDeleteView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'students'

urlpatterns = [
    path('', StudentsView.as_view() , name='students'),
    path('user_delete/<int:pk>/', UserDeleteView.as_view() , name= 'user_delete')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
