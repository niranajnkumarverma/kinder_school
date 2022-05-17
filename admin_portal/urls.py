
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('', include('admin_portal.admin.urls' , namespace="home")),
    path('orders/', include('admin_portal.order.urls' , namespace="orders")),
    path('products/', include('admin_portal.products.urls' , namespace="products")),
    path('students/', include('admin_portal.students.urls' , namespace="students")),
    path('teachers/', include('admin_portal.teachers.urls' , namespace="teachers")),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
