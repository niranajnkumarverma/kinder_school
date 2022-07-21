
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from admin_portal.principals.views import ChangePasswordView, PrincipalProfileView, PrincipalUpdateProfile, PrincipalView, UserDeactivateView, UserDeleteView, load_cities, load_state, principal_render_pdf_view


app_name = 'principals'

urlpatterns = [
    path('principals_list/', PrincipalView.as_view() , name='principals_list'),
    path('ajax/load-state/', load_state, name='ajax_load_state'), # AJAX
    path('ajax/load-cities/',load_cities, name='ajax_load_cities'), # AJAX
    path('principal-pdf/<pk>/',principal_render_pdf_view, name='principal-pdf-view'), 
    path('principal_profile/', PrincipalProfileView.as_view(), name='principal_profile'),
    path('user_account/', UserDeactivateView.as_view(), name='user_account'),
    path('user_delete/', UserDeleteView.as_view(), name='user_delete'),
    path('profile_update/', PrincipalUpdateProfile.as_view(), name='profile_update'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
