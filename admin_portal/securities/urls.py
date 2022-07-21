
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from admin_portal.principals.views import ChangePasswordView, UserDeactivateView, UserDeleteView, load_cities, load_state
from admin_portal.securities.views import SecurityProfileView, SecurityUpdateProfile, SecurityView,  security_render_pdf_view


app_name = 'securities'

urlpatterns = [
    path('security_list/', SecurityView.as_view() , name='security_list'),
    path('ajax/load-state/', load_state, name='ajax_load_state'), # AJAX
    path('ajax/load-cities/',load_cities, name='ajax_load_cities'), # AJAX
    path('security-pdf/<pk>/',security_render_pdf_view, name='security-pdf-view'), 
    path('security_profile/', SecurityProfileView.as_view(), name='security_profile'),
    path('user_account/', UserDeactivateView.as_view(), name='user_account'),
    path('user_delete/', UserDeleteView.as_view(), name='user_delete'),
    path('profile_update/', SecurityUpdateProfile.as_view(), name='profile_update'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
