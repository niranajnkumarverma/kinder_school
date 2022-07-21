"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('devices', FCMDeviceAuthorizedViewSet)
from django.views.generic import TemplateView
# from usernotifier.views import HomeView

urlpatterns = [
    path('djadmin/', admin.site.urls),
    path('',include('home.urls')),
    # path('', include('cms.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('admin/',include('admin_portal.urls')),
    path('account/',include('student.urls' , namespace='student')),
    path('product/',include('product.urls' , namespace='product')),
    path('order/',include('order.urls' , namespace='order')),
    path('chatbot/',include('chatbot.urls' , namespace='chatbot')),
    path('teacher/',include('teacher.urls')),
    path('principal/',include('principal.urls')),
    path('security/',include('security.urls' )),
    path('admins/',include('superadmin.urls' ,)),
 
   
    # path('chat/',include('chat.urls' , namespace='chat')),
    # path('user_notisfication/',include('usernotifier.urls' , namespace='user_notisficationy')),
  
    path("firebase-messaging-sw.js",
            TemplateView.as_view(
                template_name="firebase-messaging-sw.js",
                content_type="application/javascript",
            ),
            name="firebase-messaging-sw.js"
        ),
     
    path('api/', include(router.urls)),   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
handler404 = "school.views.page_not_found_view"
