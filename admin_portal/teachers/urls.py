from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from admin_portal.teachers.views import  ChangePasswordView, Delete_teacher,  TeacherProfileView, TeachersView, TeacherupdateProfile, UserDeactivateView, UserDeleteView, load_cities, load_state,teacher_render_pdf_view

app_name = 'teachers'

urlpatterns = [   
 
    
    path('teachers_list/', TeachersView.as_view(), name='teachers_list'),
    path('delete_teacher/<int:pk>/', Delete_teacher.as_view(), name='delete_teacher'),
    path('ajax/load-state/', load_state, name='ajax_load_state'), # AJAX
    path('ajax/load-cities/',load_cities, name='ajax_load_cities'), # AJAX
    path('teacher-pdf/<pk>/',teacher_render_pdf_view, name='teacher-pdf-view'), 
    path('teacher_profile/', TeacherProfileView.as_view(), name='teacher_profile'),
    path('user_account/', UserDeactivateView.as_view(), name='user_account'),
    path('user_delete/', UserDeleteView.as_view(), name='user_delete'),
    path('profile_update/', TeacherupdateProfile.as_view(), name='profile_update'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
