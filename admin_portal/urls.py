
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('admin_portal.admins.urls', namespace="home")),
    path('orders/', include('admin_portal.order.urls', namespace="orders")),
    path('products/', include('admin_portal.products.urls', namespace="products")),
    path('students/', include('admin_portal.students.urls', namespace="students")),
    path('teachers/', include('admin_portal.teachers.urls', namespace="teachers")),
    path('parents/', include('admin_portal.parents.urls', namespace="parents")),
    path('securities/', include('admin_portal.securities.urls', namespace="securities")),
    path('principals/', include('admin_portal.principals.urls', namespace="principals")),
    path('notifications/', include('admin_portal.notifications.urls', namespace='notifications')),
    path('newsapp/', include('newsApp.urls',  namespace='newsapp')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
