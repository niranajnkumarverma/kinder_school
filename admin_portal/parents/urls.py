
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from admin_portal.parents.views import ChangePasswordView, ParentProfileView, ParentUpdateProfile, ParentView, UserDeactivateView, UserDeleteView,  parent_render_pdf_view


app_name = 'parents'

urlpatterns = [
   
    path('parents_list/', ParentView.as_view(), name='parents_list'),
    path('parent-pdf/<pk>/', parent_render_pdf_view, name='parent-pdf-view'),
    path('parent_profile/', ParentProfileView.as_view(), name='parent_profile'),
    path('user_account/', UserDeactivateView.as_view(), name='user_account'),
    path('user_delete/', UserDeleteView.as_view(), name='user_delete'),
    path('profile_update/', ParentUpdateProfile.as_view(), name='profile_update'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
