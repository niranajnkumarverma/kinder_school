from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from admin_portal.teachers.views import  create_teacher, delete_teacher

app_name = 'teachers'
urlpatterns = [   
    # path('', Add_TeacherView.as_view(), name='add_teachers'),
    path('', create_teacher, name='add_teachers'),
    path('delete_teacher/<int:pk>/',delete_teacher, name='delete_teacher'),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
