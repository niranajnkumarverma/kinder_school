"""columbia URL Configuration

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

  
from django.urls import path
from .views import AboutView,ContactView, CourseView, EventView, GalleryView, LogoutView, SignUpView,TeacherView


# app_name = 'home'

urlpatterns = [
      path('', SignUpView.as_view(), name='signup'),
      path('teacherview/',TeacherView.as_view(), name='teacherview'),
      path('contactview/',ContactView.as_view(), name='contactview'),
      path('aboutview/',AboutView.as_view(), name='aboutview'),
      path('courseview/',CourseView.as_view(), name='courseview'),
      path('galleryview/',GalleryView.as_view(), name='galleryview'),
      path('eventview/',EventView.as_view(), name='eventview'),
      path('logout/', LogoutView.as_view(), name='logout'),
  
    
]